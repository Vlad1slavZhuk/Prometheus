#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: resize n infile outfile\n");
        return 1;
    }

    // remember size multiplier
    float n = atof(argv[1]);

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    int oldWidth = bi.biWidth;
    int oldHeight = bi.biHeight;
    int newWidth = floor(oldWidth * n);
    int newHeight = floor(oldHeight * n);

    int inPadding = (4 - (oldWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int outPadding = (4 - (newWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    bi.biHeight = newHeight;
    bi.biWidth = newWidth;
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * newWidth) + outPadding) * abs(newHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine ratio
    double widthRatio = (double) oldWidth / (double) newWidth;
    double heightRatio = (double) oldHeight / (double) newHeight;

    // allocate a memory to store one scanline
    RGBTRIPLE scanline[oldWidth * sizeof(RGBTRIPLE)];
    int cachedScanline = -1;

    // for all rows in the new image
    for (int i = 0, biHeight = abs(newHeight); i < biHeight; i++)
    {
        int row = i * heightRatio;

        if (cachedScanline != row)
        {
            fseek(inptr, sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + (((sizeof(RGBTRIPLE) * oldWidth) + inPadding) * row), SEEK_SET);
            fread(scanline, sizeof(RGBTRIPLE), oldWidth, inptr);
            cachedScanline = row;
        }

        for (int j = 0; j < newWidth; j++)
        {
            int column = j * widthRatio;
            fwrite(&scanline[column], sizeof(RGBTRIPLE), 1, outptr);
        }

        for (int j = 0; j < outPadding; j++)
        {
            fputc(0x00, outptr);
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}