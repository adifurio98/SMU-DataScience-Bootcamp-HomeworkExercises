var data = {};

d3.json("./samples.json").then(function(inp_data){
    console.log(inp_data);
    data = inp_data // save

    makeDropdown();
}); 


function makeDropdown() {
    for (let i = 0; i < data.names.length; i++){
        let name = data.names[i];
        d3.select("#selDataset").append("option").text(name);
    }
}

function makeBar(val) {
    
}