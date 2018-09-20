var cnv;

var gif, recording = false;

function setup() {
    cnv = createCanvas(400, 400);

    var start_rec = createButton("Start Recording");
    start_rec.mousePressed(saveVid);

    var stop_rec = createButton("Stop Recording");
    stop_rec.mousePressed(saveVid);

    start_rec.position(500, 500);
    stop_rec.position(650, 500);

    setupGIF();
}

function saveVid() {
    recording = !recording;
    if (!recording) {
        gif.render();
    }
}
var x = 0;
var y = 0;

function draw() {
    background(51);
    fill(255);
    ellipse(x, y, 20, 20);
    x++;
    y++;

    if (recording) {
        gif.addFrame(cnv.elt, {
            delay: 1,
            copy: true
        });
    }
}

function setupGIF() {
    gif = new GIF({
        workers: 5,
        quality: 20
    });
    gif.on('finished', function(blob) {
        window.open(URL.createObjectURL(blob));