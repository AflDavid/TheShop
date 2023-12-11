package org.example;
import java.util.Collections;
import java.util.Scanner;
import java.util.*;

public class ToolShop {
    public static void main(String[] args) {
        // Observer Pattern: Creating a product and an observer
        Product hammer = new Product("Hammer", 10, 19.99);
        StockUpdater stockUpdater = new StockUpdater();
        hammer.addObserver(stockUpdater);

        // Mediator Pattern: Creating a mediator and registering components
        OrderMediator orderMediator = new OrderMediator();
        orderMediator.registerObserver(stockUpdater);

        // Strategy Pattern: Creating payment strategies
        PaymentStrategy cashPayment = new CashPayment();
        PaymentStrategy cardPayment = new CardPayment();
        PaymentStrategy loanPayment = new LoanPayment(12);
        PaymentStrategy cryptoPayment = new CryptoPayment();

        // Command Pattern: Creating commands
        Command addToCartCommand = new AddToCartCommand(hammer, 0);  // The quantity will be input later

        // Composite Pattern: Creating orders
        CompositeOrder compositeOrder = new CompositeOrder();

        // Builder Pattern: Creating director and builder
        OrderDirector orderDirector = new OrderDirector(new ConcreteOrderBuilder());

        // Building the order
        orderDirector.constructOrder();

        // Displaying the built order
        System.out.println("Order details:");
        compositeOrder.display();

        // Performing the add to cart operation
        System.out.println("Performing the add to cart operation");
        addToCartCommand.execute();

        // Displaying the cart
        System.out.println("Cart details:");
        compositeOrder.display();

        // Mediating the stock update
        orderMediator.mediate("Stock updated", hammer);

        // Completing the order (executing all commands)
        System.out.println("Completing the order");
        Command completeOrderCommand = new CompleteOrderCommand(Collections.singletonList(addToCartCommand));
        completeOrderCommand.execute();

        // Payment strategy execution
        System.out.println("Payment strategy execution");
        cashPayment.pay(compositeOrder.getTotalPrice());
        cardPayment.pay(compositeOrder.getTotalPrice());
        loanPayment.pay(compositeOrder.getTotalPrice());
        cryptoPayment.pay(compositeOrder.getTotalPrice());
    }
}