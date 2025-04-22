import java.util.Random;
import java.util.Scanner;

class Player {
    private int health;

    public Player() {
        this.health = 100;
    }

    public int getHealth() {
        return health;
    }

    public boolean isAlive() {
        return health > 0;
    }

    public void takeDamage(int dmg) {
        health -= dmg;
        if (health < 0) {
            health = 0;
        }
    }

    public void heal(int amt) {
        health += amt;
        if (health > 100) {
            health = 100;
        }
    }
}

public class Sundoo {
    private Player player;
    private int timeRemaining;
    private Scanner scanner;
    private Random random;

    public Sundoo() {
        this.player = new Player();
        this.timeRemaining = 12; // 12 tundi ellujäämiseks
        this.scanner = new Scanner(System.in);
        this.random = new Random();
    }

    public void startGame() {
        System.out.println("Tere tulemast Sundöö ellujäämismängu!");
        System.out.println("Sinu eesmärk on ellu jääda järgmised 12 tundi...\n");

        while (timeRemaining > 0 && player.isAlive()) {
            System.out.println("Jäänud tunde: " + timeRemaining);
            System.out.println("Sinu elu: " + player.getHealth());
            playHour();
            timeRemaining--;
        }

        if (player.isAlive()) {
            System.out.println("\nPalju õnne! Sa jäid ellu!");
        } else {
            System.out.println("\nSa said surma. Mäng läbi.");
        }
    }

    private void playHour() {
        String[] events = {
            "Sind rünnatakse!", 
            "Leidsid medkiti!", 
            "Kuulsid müra ja peitsid end."
        };

        int eventIndex = random.nextInt(events.length);
        String event = events[eventIndex];

        System.out.println("\nSündmus: " + event);
        System.out.println("Vali tegevus:");
        System.out.println("1. Jookse");
        System.out.println("2. Võitle");
        System.out.println("3. Peitu");
        System.out.print(">> ");

        int choice = scanner.nextInt();

        switch (eventIndex) {
            case 0: 
                if (choice == 2) {
                    System.out.println("Sa võitlesid tagasi, kuid said viga.");
                    player.takeDamage(20);
                } else {
                    System.out.println("Sa ei võidelnud ja kaotasid rohkem elu.");
                    player.takeDamage(30);
                }
                break;
            case 1: // leid
                System.out.println("Sa said tervist juurde!");
                player.heal(15);
                break;
            case 2: // peitumine
                if (choice == 3) {
                    System.out.println("Peitusid edukalt.");
                } else {
                    System.out.println("Vale otsus, natuke kahju.");
                    player.takeDamage(10);
                }
                break;
        }

        System.out.println();
    }

    public static void main(String[] args) {
        Sundoo game = new Sundoo();
        game.startGame();
    }
}
