const fs = require('fs');
const readline = require('readline');

class Pencil {
    constructor(id, brand, color, length) {
        this.id = id;
        this._brand = brand;
        this._color = color;
        this._length = length;
    }

    get brand() {
        return this._brand;
    }

    get color() {
        return this._color;
    }

    get length() {
        return this._length;
    }

    set brand(newBrand) {
        this._brand = newBrand;
    }

    set color(newColor) {
        this._color = newColor;
    }

    set length(newLength) {
        this._length = newLength;
    }
}

class ReadPencil {
    static read(filename) {
        try {
            const jsonString = fs.readFileSync(filename, 'utf8');
            const pencilData = JSON.parse(jsonString);
            return pencilData.map(p => new Pencil(p.id, p._brand, p._color, p._length));
        } catch (error) {
            throw new Error(`Error reading ${filename}: ${error.message}`);
        }
    }
}

class SavePencil {
    static save(pencils, filename) {
        if (!Array.isArray(pencils) || !pencils.every(p => p instanceof Pencil)) {
            throw new Error("The object to save is not an array of Pencil instances.");
        }
        const json = JSON.stringify(pencils);
        fs.writeFileSync(filename, json);
        console.log(`Pencils saved to ${filename}`);
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion(query) {
    return new Promise(resolve => rl.question(query, resolve));
}

async function main() {
    const pencils = [];
    let id = 1;

    while (true) {
        const brand = await askQuestion(`Enter brand for pencil ${id}: `);
        const color = await askQuestion(`Enter color for pencil ${id}: `);
        const length = await askQuestion(`Enter length for pencil ${id}: `);

        pencils.push(new Pencil(id, brand, color, parseFloat(length)));

        const another = await askQuestion('Do you want to add another pencil? (yes/no): ');
        if (another.toLowerCase() !== 'yes') {
            break;
        }

        id++;
    }

    const filename = 'pencil.json';
    SavePencil.save(pencils, filename);

    const readPencils = ReadPencil.read(filename);

    console.log("Read Pencils:", readPencils);

    rl.close();
}

main();
