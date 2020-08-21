    var url="http://127.0.0.1:5000";
    //Function to generate Elbow Plot data
    
    function elbowPointLocate()
    {
    $.getJSON(url + '/elbowPointLocate', {

  		  }, function(d) {
  		  	console.log(d)
  		  	createLineChart(d.data,"k","Distortion")
  		  });
  		  return false;
    }
    function drawScreeOriginal()
    {
    $.getJSON(url + '/drawScreeOriginal', {

  		  }, function(d) {
  		  	console.log(d)
  		  	createIntrinsicScree(d.data,"Component","Value")
  		  });
  		  return false;
    }
    //Function to generate Scree plot for PCA radom sampled data drawScreePCAStratified
    function createPlotScree()
    {
    $.getJSON(url + '/drawScreeIntrinsic', {

  		  }, function(d) {
          console.log("Hello there")
  		  	console.log(d)
  		  	createIntrinsicScree(d.data,"Component","Value")
  		  });
  		  return false;
    }
    function drawScreePCAStratified()
    {
    $.getJSON(url + '/drawScreePCAStratified', {

  		  }, function(d) {
          console.log("Hello there")
  		  	console.log(d)
  		  	createIntrinsicScree(d.data,"Component","Value")
  		  });
  		  return false;
  	}
    

    
    function generateScreePlotForMDSEuc()
    {
    $.getJSON(url + '/generateScreePlotForMDSEuc', {

        }, function(d) {
          console.log(d)
          createLineChart(d.data,"Component1","Component2")
        });
        return false;
    }
    
    function generateScreePlotForMDSEucStratified()
    {
    $.getJSON(url + '/generateScreePlotForMDSEucStratified', {

        }, function(d) {
          console.log(d)
          createLineChart(d.data,"Component1","Component2")
        });
        return false;
    }
    
    function drawScatterOriginal()
    {
    $.getJSON(url + '/drawScatterOriginal', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"PCA","PCA","N")
        });
        return false;
    }
    function ScatterPlotPCA()
    {
    $.getJSON(url + '/ScatterPlotPCA', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"PCA","PCA","N")
        });
        return false;
    }
    
    function ScatterPlotPCAStratified()
    {
    $.getJSON(url + '/ScatterPlotPCAStratified', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"PCA","PCA","Y")
        });
        return false;
    }
   
    function ScatterPlotMDS()
    {
    $.getJSON(url + '/ScatterPlotMDS', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"MDS","MDS","N")
        });
        return false;
    }
    function drawMDSOriginal()
    {
    $.getJSON(url + '/drawMDSOriginal', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"MDS","MDS","N")
        });
        return false;
    }
    
    function ScatterPlotMDSStratified()
    {
    $.getJSON(url + '/ScatterPlotMDSStratified', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"MDS","MDS","Y")
        });
        return false;
    }
    
    function ScatterPlotMDSCorr()
    {
    $.getJSON(url + '/ScatterPlotMDSCorr', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"MDS","MDS","N")
        });
        return false;
    }
    function drawMDSCorrOriginal()
    {
    $.getJSON(url + '/drawMDSCorrOriginal', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"MDS","MDS","N")
        });
        return false;
    }
    
    function ScatterPlotMDSCorrStratified()
    {
    $.getJSON(url + '/ScatterPlotMDSCorrStratified', {

        }, function(d) {
          console.log(d)
          createScatterPlot(d.data,"MDS","MDS","Y")
        });
        return false;
    }
    
    function stratifiedScatterPlotMatrix()
    {
    $.getJSON(url + '/stratifiedScatterPlotMatrix', {

        }, function(d) {
          console.log(d)
          createScatterPlotMatrix(d.data)
        });
        return false;
    }
    function RandomSamplingMatrix()
    {
    $.getJSON(url + '/RandomSamplingMatrix', {

        }, function(d) {
          console.log(d)
          createScatterPlotMatrix(d.data)
        });
        return false;
    }
    function originalDataMatrix()
    {
    $.getJSON(url + '/originalDataMatrix', {

        }, function(d) {
          console.log(d)
          createScatterPlotMatrix(d.data)
        });
        return false;
    }
    

    function createIntrinsicScree(data,xLabel,yLabel)
    {

      d3.selectAll("g").remove();

        console.log(data);
        var svg = d3.select("svg"),
        width = svg.attr("width")-100 ,
        height = svg.attr("height") -100
        svg.attr("align","center");

    var xScale = d3.scaleLinear()
        .domain([d3.min(data,function(d){ return d.x;}), d3.max(data,function(d){ return d.x+1;})])
        .range([0, width]).nice(); 

    var yScale = d3.scaleLinear()
        .domain([0, d3.max(data,function(d){return  d.y;})]) 
        .range([height, 0]).nice(); // output

    var line = d3.line()
        .x(function(d) { return xScale(d.x); }) 
        .y(function(d) { return yScale(d.y); }) 
    var lines = d3.line()
    .x(function(d) { return xScale(d.x); }) 
    .y(function(d) { return yScale(d.z); }) 

    var lin = d3.line()
    .x(function(d) { return 350; }) 
    .y(function(d) { return yScale(d.y) + 70; }) 

    var lis = d3.line()
    .x(function(d) { return xScale(d.x) - 10; }) 
    .y(function(d) { return 109.59090909090907; }) 

    var g=  svg.append("g")
        .attr("transform", "translate(" + 90 + "," + 30 + ")")
        .attr("align","center");
    
        

    g.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(xScale).tickSize(-height))
          .append("text")
          .attr("y", height - 350)
          .attr("x", width - 100)
          .attr("text-anchor", "end")
          .style("fill", "#401400")
          .style("font-weight","bold")
          .attr("font-size", "15px")
          .text(xLabel);

    g.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(yScale).tickSize(-width)) 
        .append("text")
        .attr("y", 6)
        .attr("dy", "-5.1em")
        .attr("transform", "rotate(-90)")
        .attr("text-anchor", "end")
        .style("fill", "#401400")
        .style("font-weight","bold")
        .attr("font-size", "15px")
        .text(yLabel);

    // Append the path, bind the data, and call the line generator
    g.append("path")
        .datum(data) //  Binds data to the line
        .attr("class", "line") // Assign a class for styling
        .attr("d", line); //  Calls the line 
    g.append("path")
    .datum(data) //  Binds data to the line
    .attr("class", "line") // Assign a class for styling
    .attr("d", lin); //  Calls the line generator
    

    //  Appends a circle for each datapoint
    g.selectAll(".dot")
        .data(data)
      .enter().append("circle")
        .attr("class", "dot") // Assign a class for styling
        .attr("cx", function(d) { return xScale(d.x) })
        .attr("cy", function(d) { return yScale(d.y) })
        .attr("r", 4);
    g.selectAll('rect') // Get all the rectangles in the svg
    .data(data) // Bind the 5 data points
    .enter() // Grab the 5 'new' data points
    .append('rect') // Add a rectangles for each 'new' data point
    .attr('x', function(d) { return xScale(d.x)}) // Begin setting attributes
    .attr('y', function(d) { return yScale(d.z)})
    .attr('height', function(d) { return height - yScale(d.z);})
    .attr('width', function(d) {
      return  66; // data point * 2 pixels wide
    })
    


        


        
    }
    function createLineChart(data,xLabel,yLabel)

    	{
        d3.selectAll("g").remove();
    //    debugger;
        console.log(data);
        var svg = d3.select("svg"),
        width = svg.attr("width")-100 ,
        height = svg.attr("height") -100
        svg.attr("align","center");

    var xScale = d3.scaleLinear()
        .domain([d3.min(data,function(d){ return d.x;}), d3.max(data,function(d){ return d.x;})])
        .range([0, width]).nice(); // output

    var yScale = d3.scaleLinear()
        .domain([0, d3.max(data,function(d){return  d.y;})]) 
        .range([height, 0]).nice(); // output

    var line = d3.line()
        .x(function(d) { return xScale(d.x); }) 
        .y(function(d) { return yScale(d.y); }) 
    
    var g=  svg.append("g")
        .attr("transform", "translate(" + 100 + "," + 50 + ")");
    
        

    g.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(xScale).tickSize(-height))
          .append("text")
          .attr("y", height - 350)
          .attr("x", width - 100)
          .attr("text-anchor", "end")
          .style("fill", "#401400")
          .style("font-weight","bold")
          .attr("font-size", "25px")
          .text(xLabel);

    g.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(yScale).tickSize(-width)) 
        .append("text")
        .attr("y", 6)
        .attr("dy", "-5.1em")
        .attr("transform", "rotate(-90)")
        .attr("text-anchor", "end")
        .style("fill", "#401400")
        .style("font-weight","bold")
        .attr("font-size", "15px")
        .text(yLabel);

    
    g.append("path")
        .datum(data) 
        .attr("class", "line") 
        .attr("d", line); 
   
    
    g.selectAll(".dot")
        .data(data)
      .enter().append("circle")
        .attr("class", "dot") 
        .attr("cx", function(d) { return xScale(d.x) })
        .attr("cy", function(d) { return yScale(d.y) })
        .attr("r", 4);

        

    	}

      function createScatterPlot(data,xLabel,yLabel,clusterFlag)

      	{
          d3.selectAll("g").remove();
        //  debugger;
        console.log(data);
        var svg = d3.select("svg"),
        width = svg.attr("width")-100 ,
        height = svg.attr("height") -100
        svg.attr("align","center");

      var xScale = d3.scaleLinear()
          .domain([d3.min(data,function(d){ return d.x;}), d3.max(data,function(d){ return d.x;})])// input
          .range([0, width]).nice(); 


      var yScale = d3.scaleLinear()
          .domain([d3.min(data,function(d){return  d.y;}), d3.max(data,function(d){return  d.y;})]) // input
          .range([height, 0]).nice();


      var color=d3.scaleOrdinal(d3.schemeCategory10);

      var g=  svg.append("g")
          .attr("transform", "translate(" + 130 + "," + 70 + ")");

      g.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(xScale).tickSize(-height))
          .append("text")
          .attr("y", height - 350)
          .attr("x", width - 100)
          .attr("text-anchor", "end")
          .style("fill", "#401400")
          .style("font-weight","bold")
          .attr("font-size", "15px")
          .text(xLabel);

      g.append("g")
          .attr("class", "y axis")
          .call(d3.axisLeft(yScale).tickSize(-width ))
          .append("text")
          .attr("y", 6)
          .attr("dy", "-5.1em")
          .attr("transform", "rotate(-90)")
          .attr("text-anchor", "end")
          .style("fill", "#401400")
          .style("font-weight","bold")
          .attr("font-size", "15px")
          .text(yLabel);

      g.selectAll(".dot")
          .data(data)
        .enter().append("circle")
          .attr("cx", function(d) { return xScale(d.x) })
          .attr("cy", function(d) { return yScale(d.y) })
          .style("fill", function(d) { return color(d.cluster);})
          .attr("r", 4);
    if(clusterFlag=="Y"){
          var legend = g.selectAll(".legend")
          .data(color.domain())
        .enter().append("g")
          .attr("class", "legend")
          .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

      legend.append("rect")
          .attr("x", width - 50)
          .attr("width", 20)
          .attr("height", 20)
          .style("fill", color);

      legend.append("text")
          .attr("x", width - 50)
          .attr("y", 9)
          .attr("dy", ".35em")
          .style("text-anchor", "end")
          .text(function(d) {return "Group"+ d; });

        }

      	}
     
        function createScatterPlotMatrix(data){
              d3.selectAll("g").remove();

              var size=230,
              padding=20;
              
              var columnsDomain = {},
               columns = d3.keys(data[0]).filter(function(d) { return d !== "clusters"; }),
               n = columns.length;
               columns.forEach(function(column) {
                 columnsDomain[column] = d3.extent(data, function(d) { return d[column]; });
               });

               var svg = d3.select("svg")
                   .attr("width", size * n + padding)
                   .attr("height", size * n + padding)
                   .attr("align","center");

               var color=d3.scaleOrdinal(d3.schemeCategory10);

               var xScale = d3.scaleLinear()
            .range([padding / 2, size - padding / 2]);

              var yScale = d3.scaleLinear()
                  .range([size - padding / 2, padding / 2]);

              var g= svg.append("g")
                   .attr("transform", "translate(" + padding + "," + padding / 2 + ")");

               g.selectAll(".x.axis")
                   .data(columns)
                 .enter().append("g")
                   .attr("class", "x axis")
                   .attr("transform", function(d, i) { return "translate(" + (n - i - 1) * size + ",0)"; })
                   .each(function(d) { xScale.domain(columnsDomain[d]); d3.select(this).call(d3.axisBottom(xScale).tickSize(size*n)); });

               g.selectAll(".y.axis")
                   .data(columns)
                 .enter().append("g")
                   .attr("class", "y axis")
                   .attr("transform", function(d, i) { return "translate(0," + i * size + ")"; })
                   .each(function(d) { yScale.domain(columnsDomain[d]); d3.select(this).call(d3.axisLeft(yScale).tickSize(-size*n)); });
              
               var cell = g.selectAll(".cell")
                   .data(cross(columns, columns))
                 .enter().append("g")
                   .attr("class", "cell")
                   .attr("transform", function(d) {return "translate(" + (n - d.i - 1) * size + "," + d.j * size + ")"; })
                   .each(plot);

              
               cell.filter(function(d) { return d.i === d.j; }).append("text")
                   .attr("x", padding)
                   .attr("y", padding)
                   .attr("dy", ".71em")
                   .text(function(d) { return d.x; });
               
               function plot(p) {
                 var cell = d3.select(this);

                 xScale.domain(columnsDomain[p.x]);
                 yScale.domain(columnsDomain[p.y]);

                 cell.append("rect")
                     .attr("class", "frame")
                     .attr("x", padding / 2)
                     .attr("y", padding / 2)
                     .attr("width", size - padding)
                     .attr("height", size - padding);

                 cell.selectAll("circle")
                     .data(data)
                   .enter().append("circle")
                     .attr("cx", function(d) { return xScale(d[p.x]); })
                     .attr("cy", function(d) { return yScale(d[p.y]); })
                     .attr("r", 6)
                     .style("fill", function(d) { return color(d.clusters); });
               }
            }
        function cross(a, b) {
              var c = [], n = a.length, m = b.length, i, j;
              for (i = -1; ++i < n;) for (j = -1; ++j < m;) c.push({x: a[i], i: i, y: b[j], j: j});
              return c;
        }
