#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

class Player {
private:
    int hp;
    int energy;
    int food;

public:
    Player(int hp, int energy, int food)
        : hp(hp), energy(energy), food(food) {}

    void status() const {
        cout << "\n[ Staatus ] HP: " << hp << " | Energia: " << energy << " | Toit: " << food << endl;
    }

    void rest() {
        if (food > 0) {
            food--;
            energy += 3;
            cout << "Sa puhkasid. Energia taastatud (+3)." << endl;
        } else {
            cout << "Pole piisavalt toitu puhkamiseks!" << endl;
        }
    }

    void takeDamage(int dmg) {
        hp -= dmg;
        if (hp < 0) hp = 0;
        cout << "Said kahju: -" << dmg << " HP." << endl;
    }

    void useEnergy(int amount) {
        energy -= amount;
        if (energy < 0) energy = 0;
    }

    void addFood(int amount) {
        food += amount;
    }

    bool isAlive() const {
        return hp > 0 && energy > 0;
    }
};

enum EventType {
    NONE,
    DANGER,
    FOOD_FOUND
};

EventType randomEvent() {
    int roll = rand() % 3;
    if (roll == 0) return DANGER;
    else if (roll == 1) return FOOD_FOUND;
    return NONE;
}

void processEvent(Player& player) {
    EventType event = randomEvent();
    switch (event) {
        case DANGER:
            cout << "⚠️  Ohtlik sündmus! Sa sattusid rünnaku alla." << endl;
            player.takeDamage(3);
            player.useEnergy(1);
            break;
        case FOOD_FOUND:
            cout << "🍖 Leidsid toidutagavara! (+1 toidukord)" << endl;
            player.addFood(1);
            break;
        default:
            cout << "Kõik on vaikne... midagi ei juhtunud." << endl;
    }
}

int main() {
    srand(static_cast<unsigned>(time(0)));

    Player player(10, 5, 2);
    int day = 1;

    cout << "🎮 Tere tulemast mängu 'Sundöö'!" << endl;
    cout << "Eesmärk: jää ellu nii kaua kui võimalik, tehes strateegilisi otsuseid.\n";

    while (player.isAlive()) {
        cout << "\n========== Päev " << day << " ==========" << endl;
        player.status();

        cout << "Valikud:\n";
        cout << "1. Puhka (kasutab toitu, taastab energiat)\n";
        cout << "2. Riskida sündmusega (võib leida toitu või saada kahju)\n";
        cout << "3. Mitte teha midagi (jätad päeva vahele)\n";
        cout << "Vali (1-3): ";

        int choice;
        cin >> choice;

        switch (choice) {
            case 1:
                player.rest();
                break;
            case 2:
                processEvent(player);
                break;
            case 3:
                cout << "Sa otsustasid mitte midagi teha..." << endl;
                player.useEnergy(1);
                break;
            default:
                cout << "❌ Vigane valik." << endl;
                continue;
        }

        // Iga päev energiakulutus
        player.useEnergy(1);
        day++;
    }

    cout << "\n💀 Mäng läbi. Sa ei jäänud ellu." << endl;
    cout << "Ellujäämispäevad: " << day - 1 << endl;
    return 0;
}
