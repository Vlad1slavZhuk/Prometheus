package com.tasks5.command;

public class Application {
	static class Help implements Command {

        @Override
        public void execute() {
            System.out.println("Help executed");
        }
    }

    static class Echo implements Command {
        private String text;

        public Echo(String text) {
            this.text = text;
        }

        @Override
        public void execute() {
            System.out.println(text);
        }
    }

    static class Date implements Command {

        @Override
        public void execute() {
            System.out.println(System.currentTimeMillis());
        }
    }

    static class Exit implements Command {

        @Override
        public void execute() {
            System.out.println("Goodbye!");
        }
    }


    public static void main(String[] args) {
        if (args == null || args.length == 0)
            System.out.println("Error");

        else {
            Command command;
            switch (args[0]) {
                case "help":
                    if (args.length == 1) {
                        command = new Help();
                        command.execute();
                    } else
                        System.out.println("Error");
                    break;
                case "echo":
                    if (args.length == 2) {
                        command = new Echo(args[1]);
                        command.execute();
                    } else
                        System.out.println("Error");
                    break;
                case "date":
                    if (args.length == 2 && args[1].equals("now")) {
                        command = new Date();
                        command.execute();
                    } else
                        System.out.println("Error");
                    break;
                case "exit":
                    if (args.length == 1) {
                        command = new Exit();
                        command.execute();
                    } else
                        System.out.println("Error");
                    break;
                default:
                    System.out.println("Error");
            }
        }
    }
}