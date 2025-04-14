var nameList = [
    "Time",
    "Past",
    "Future",
    "Dev",
    "Fly",
    "Flying",
    "Soar",
    "Soaring",
    "Power",
    "Falling",
    "Fall", "Jump"
]

class Platform{
    constructor(resources, floorStatus) {
        this.resources = resources;
        this.floorStatus = floorStatus;
    }

    consume(amount) {
        this.resources -=amount
    }
}


class Floor{
    constructor(lvl, peopleCount ) {
        this.lvl = lvl;
        this.peopleCount = peopleCount;
    }

    process_Platform(platform) {
        console.log("Korrus: ", this.lvl);
        this.peopleCount.forEach((person) => {
            person.makeDecision(platform)
        });
        console.log("Resurside jaak: ", platform.resources);
    }
}

class Person {
    constructor(name, pertcent) {
        this.name = name;
        this.pertcent = pertcent;
    };

    makeDecision(platform) {
        let ranNum = Math.random * 100;
        if (ranNum < this.pertcent && platform.resources > 0) {
            const eatAmount = 10;
            platform.consume(eatAmount);
            console.log(this.name, "sõid ", eatAmount, "toitu");
            
        }
    }
}

let floors = []
for(let i = 0; i<=10; i++) {
    let person1 = new Person(nameList[Math.floor(Math.random() * nameList.length)],
        Math.floor(Math.random() *100) + 1 + "%"        
    );

    let person2= new Person(nameList[Math.floor(Math.random() * nameList.length)],
        Math.floor(Math.random() *100) + 1 + "%"        
    );

    let floor = new Floor(i, [person1, person2]);

    floors.push(floor);

}

console.log(floors)

let platform = new Platform(100);

floors.forEach((floor) => {
    floor.process_Platform(platform)
})