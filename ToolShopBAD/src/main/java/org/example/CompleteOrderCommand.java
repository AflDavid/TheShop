package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

class CompleteOrderCommand implements Command {
    private List<Command> orderCommands;

    public CompleteOrderCommand(List<Command> orderCommands) {
        this.orderCommands = orderCommands;
    }

    @Override
    public void execute() {
        // Execute all commands in the order
        orderCommands.forEach(Command::execute);
    }
}