function buildDisplay(sample) {
    d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json")
        .then((response) => {
        
        var sampleData = response.samples.filter(sampleObj => sampleObj.id == sample)[0];
        let otu_ids = sampleData.otu_ids;
        let otu_labels = sampleData.otu_labels;
        let sample_values = sampleData.sample_values;


        let yLabel = otu_ids.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse();
        let barData = [
            {
                y: yLabel,
                x: sample_values.slice(0, 10).reverse(),
                text: otu_labels.slice(0, 10).reverse(),
                type: "bar",
                orientation: "h",
            }
        ];

        let barLayout = {
        title: "Top 10 Bacteria Cultures Found",
        margin: { t: 30, l: 150 }
        };

        Plotly.newPlot("bar", barData, barLayout);


        // Build a Bubble Chart
        let bubbleLayout = {
            title: "Bacteria Cultures Per Sample",
            margin: { t: 0 },
            hovermode: "closest",
            xaxis: { title: "OTU ID" },
            margin: { t: 30}
        };
        let bubbleData = [
            {
            x: otu_ids,
            y: sample_values,
            text: otu_labels,
            mode: "markers",
            marker: {
                size: sample_values,
                color: otu_ids,
                colorscale: "Earth"
            }
            }
        ];
        Plotly.newPlot("bubble", bubbleData, bubbleLayout);

        // response doesnt exist here
        let metadata = response.metadata.filter(sampleObj => sampleObj.id == sample)[0];
        let PANEL = d3.select("#sample-metadata");
        PANEL.html("");
        for (key in metadata){
          PANEL.append("h6").text(`${key.toUpperCase()}: ${metadata[key]}`);
        };
    });
    
}

function main() {
    d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json").then((data) => {
        let sampleNames = data.names;
        for (let i = 0; i < sampleNames.length; i++){
            d3.select("#selDataset")
                .append("option")
                .text(sampleNames[i])
                .property("value", sampleNames[i]);
        };
        buildDisplay(sampleNames[0]);
    });
}

function optionChanged(newSample) {
    buildDisplay(newSample);
}

main()
