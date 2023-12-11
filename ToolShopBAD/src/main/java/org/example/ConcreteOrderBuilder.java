package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Builder Pattern: Concrete Builder
class ConcreteOrderBuilder implements OrderBuilder {
    private CompositeOrder order = new CompositeOrder();

    @Override
    public void buildProductOrder(String productName, int quantity) {
        // Retrieve the product from the inventory (not shown here)
        Product product = new Product(productName, 10, 19.99);
        ProductOrder productOrder = new ProductOrder(product, quantity);
        order.addOrderComponent(productOrder);
    }

    @Override
    public void buildPaymentStrategy(PaymentStrategy paymentStrategy) {
        // Set payment strategy for the entire order
        // (In a more realistic scenario, this might involve multiple payment strategies for each item)
        System.out.println("Payment strategy set");
    }
}