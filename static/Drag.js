let press = 0;
document.onkeypress = function (e) {
	console.log(press++);
}
//let temp = document.getElementsByClassName("draggable");


document.body.addEventListener("mousemove", release);
document.body.addEventListener("mouseup", touchStart);
for( let i = 0; i<document.getElementsByClassName("draggable").length; i++){
	document.getElementsByClassName("draggable")[i].addEventListener("mousedown", click);
	//document.getElementsByClassName("draggable")[i].addEventListener("mouseup", touchStart);
	//document.getElementsByClassName("draggable")[i].addEventListener("mouseout", touchStart);
}

targets = document.getElementsByClassName("draggable");
//targets[0].style.left = "100px"
/*
document.getElementsByClassName("draggable")[0].addEventListener("mousedown", click);
document.getElementsByClassName("draggable")[0].addEventListener("mousemove", release);
document.getElementsByClassName("draggable")[0].addEventListener("mouseup", touchStart);
document.getElementsByClassName("draggable")[0].addEventListener("mouseout", touchStart);

/*
document.getElementsByClassName("draggable")[1].addEventListener("dragstart", click);
document.getElementsByClassName("draggable")[1].addEventListener("dragend", release);
document.getElementsByClassName("draggable")[1].addEventListener("drag", touchStart);
*/




let startDiffX = [];
let startDiffY = [];
for( let i = 0; i<targets.length; i++){
	startDiffX.push(0);
	startDiffY.push(0);

	//targets[i].style.left = Math.round(Math.random()*1200 - 200) + "px"
	//targets[i].style.top = Math.round(Math.random()*800 - 500) + "px"

}
let down = false
let target = null;
function click(e) {
	target = e.target;
	for( let i = 0; i<targets.length; i++){
		startDiffX[i] = e.clientX - parseInt(targets[i].style.left || 0);
		startDiffY[i] = e.clientY - parseInt(targets[i].style.top || 0);
	}
	//startDiffX = e.clientX - parseInt(target.style.left || 0);
	//startDiffY = e.clientY - parseInt(target.style.top || 0);
	//e.srcElement.innerHTML = "Ahhhhhhhhhhhhhhhhhhh";
	down = true;
}


function release(e) {
	if(down){
		//dX = e.movementX;
		//dY = e.movementY;
		//console.log(e.movementX, e.clientX, e.movementY, e.clientY);
		//console.log(target)
		if(target !== null){
			//target.style.left = (parseFloat(target.style.left || 0) + dX) + "px";
			//target.style.top = (parseFloat(target.style.top || 0) + dY) + "px";
			//target.style.left = (e.clientX - startDiffX) + "px";
			//target.style.top = (e.clientY - startDiffY) + "px";
			for( let i = 0; i<targets.length; i++){
				targets[i].style.left = (e.clientX - startDiffX[i]) + "px";
				targets[i].style.top = (e.clientY - startDiffY[i]) + "px";
				
			}
		}
		
	}
}

function dance(){
	for( let i = 0; i<targets.length; i++){
		targets[i].style.left = Math.round(Math.random()*1200 - 200) + "px"
		targets[i].style.top = Math.round(Math.random()*800 - 500) + "px"
	}

}

function add(num){
	console.log(document.body)
	for( let i = 0; i<num; i++){
		console.log("Hi")
	}
}

function touchStart(e) {
	if(down){
	
	}
	target = null;
	down = false;
	console.log("AH")
}


function dragElement(elmnt) {
	console.log("dragging")
}

function dragMouseDown(e) {
	console.log("DRAG")
}