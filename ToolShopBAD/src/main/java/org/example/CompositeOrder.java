package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

// Composite Pattern: Composite class
class CompositeOrder implements OrderComponent {
    private List<OrderComponent> orderComponents = new ArrayList<>();

    public void addOrderComponent(OrderComponent orderComponent) {
        orderComponents.add(orderComponent);
    }

    @Override
    public void display() {
        orderComponents.forEach(OrderComponent::display);
    }

    public double getTotalPrice() {
        double totalPrice = 0;
        for (OrderComponent component : orderComponents) {
            if (component instanceof ProductOrder) {
                ProductOrder productOrder = (ProductOrder) component;
                totalPrice += productOrder.getProduct().getPrice() * productOrder.getQuantity();
            }
        }
        return totalPrice;
    }
}