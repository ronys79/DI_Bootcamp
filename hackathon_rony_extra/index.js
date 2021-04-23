// https://www.youtube.com/watch?v=Wh2kVSPi_sE
// health bar start
class HealthBar {
    constructor(x, y, w, h, maxHealth, color,) {
      this.x = x;
      this.y = y;
      this.w = w;
      this.h = h;
      this.maxHealth = maxHealth;
      this.maxWidth = w;
      this.health = maxHealth;
      this.color = color;
    }
  
    show(context) {
      // border around red bar
      context.lineWidth = 4;
      context.strokeStyle = "darkgrey";
      context.fillStyle = this.color;
      context.fillRect(this.x, this.y, this.w, this.h);
      context.strokeRect(this.x, this.y, this.maxWidth, this.h);
    }
  
    updateHealth(val) {
      if (val >= 0) {
        this.health = val;
        this.w = (this.health / this.maxHealth) * this.maxWidth;
      }
    }
  }

  // health bar end

const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");

// style-size of the outer canvas of health bar

const width = canvas.width = 80;
const height = canvas.height = 40;

// use this to position bar on top of page, set to top right margin of page with inner height /2 of canvas
canvas.style.marginTopRight = window.innerHeight / 2 - height / 2 + "px";

// total life counter
let health = 100;

// style-size of the actual health bar
const healthBarWidth = 70;
const healthBarHeight = 20;
const x = width / 2 - healthBarWidth / 2;
const y = height / 2 - healthBarHeight / 2;

const healthBar = new HealthBar(x, y, healthBarWidth, healthBarHeight, health, "red");

const frame = function() {
  context.clearRect(0, 0, width, height);
  healthBar.show(context);
  requestAnimationFrame(frame);
}

canvas.onclick = function() {
  // health is how much HP lost per wrong answer. set at -33 per wrong answer = 3 lives
  health -= 33;
  healthBar.updateHealth(health);
};

frame();