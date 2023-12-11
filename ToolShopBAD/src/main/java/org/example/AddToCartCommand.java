package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Command Pattern: Concrete Commands
class AddToCartCommand implements Command {
    private Product product;
    private int quantity;

    public AddToCartCommand(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    @Override
    public void execute() {
        // Perform the add to cart operation
        System.out.println("Added " + quantity + " " + product.getName() + " to the cart");
    }
}