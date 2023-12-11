package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Composite Pattern: Leaf class
class ProductOrder implements OrderComponent {
    private Product product;
    private int quantity;

    public ProductOrder(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    public Product getProduct() {
        return product;
    }

    public int getQuantity() {
        return quantity;
    }

    @Override
    public void display() {
        System.out.println(quantity + " x " + product.getName() + " - $" + product.getPrice());
    }
}