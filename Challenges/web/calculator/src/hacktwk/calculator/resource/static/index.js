class Calculator {
    static a = "";
    static b = "";
    static operator = "";

    static operators = {
        "+": "add", "-": "subtract", "*": "multiply", "/": "divide"
    }

    static eval(val) {
        if (val === "EXE") {
            location.assign(`/${this.operators[this.operator]}/${this.a}/${this.b}`);
            return;
        }

        if (val === "C") {
            this.a = "";
            this.b = "";
            this.operator = "";
        } else if (["+", "-", "*", "/"].includes(val)) {
            if (this.a === "") {
                return;
            }
            this.operator = val;
        } else if (this.operator === "") {
            this.a += val;
        } else if (this.operator !== "" && this.a !== "") {
            this.b += val;
        }

        document.getElementById("result").innerText = this.a + this.operator + this.b;
    }
}