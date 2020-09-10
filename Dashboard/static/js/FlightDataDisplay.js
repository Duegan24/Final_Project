// The FlightDataDisplay contains of multiple
//     FlightDisplayPanel objects - one for each hour
//
// Each FlightDisplayPanel contains three
//     FlightDataStatusPanel objects - displays flight data and delay predict status
//
//     1 - displays a blank panel 
//     2 - displays weather data and is green if predicted delay = 0
//     2 - Displays weather data and is red if predicted delay = 12


// This object contains references to a status panel 
// The weather HTML element of the panel can be update with data
// The panel can have 
// No backgroud color - no weather data --- blank panel
// Red background color - weather data --- delayed panel
// Green background color - weather data --- on time panel
class FlightDataStatusPanel{

    constructor(id, isBlank, isOnTime){

        // Get reference to the HTML status panel
        this.panel = d3.select("#" + id + (isBlank?"_blank":isOnTime?"_on_time":"_delayed"));;

        // If the status panel is the blank panel return
        if (isBlank){
            return;
        }

        // If the HTML status panel is the on time or delayed panel
        // get refrences to the panel's data HTML elements 
        // which will be updated with weather data 
        let panelValuesIdPrefix = "#" + id + (isOnTime?"_on_time_":"_delayed_");

        this.cloudiness         = d3.select(panelValuesIdPrefix + "cloudiness");
        this.precipitation      = d3.select(panelValuesIdPrefix + "precipitation");
        this.wind               = d3.select(panelValuesIdPrefix + "wind");
        this.humidity           = d3.select(panelValuesIdPrefix + "humidity");
        this.visibility         = d3.select(panelValuesIdPrefix + "visibility");

    }

    // Display the status panel
    show(){
        this.panel.classed("hide", false);
        this.panel.classed("show", true);
    }

    // Hide the status panel
    hide(){
        this.panel.classed("show", false);
        this.panel.classed("hide", true);
    }

    // Update the status panel's weather data fields
    updatePanel(nameValueParms){

        let panelValueElement;

        for (name in nameValueParms){
            panelValueElement = this[name];
            if (panelValueElement === undefined || panelValueElement === null)
                continue;
            this[name].text(nameValueParms[name]);
        }
    }
}

// This object contains the three FlightDataStatusPanels 
// for a given flight display hour
//    Blank status panel 
//    On Time status panel
//    Delayed status panel
class FlightDataDisplayPanel {

    constructor(id){

        this.timeDisplayElement = d3.select("#" + id + "_time");

        // Create the status panel object
        this.noDataStatusPanel = new FlightDataStatusPanel(id, true, false);
        this.ontimeStatusPanel = new FlightDataStatusPanel(id, false, true);
        this.delayedStatusPanel = new FlightDataStatusPanel(id, false, false);
        this.clear();
    }

    // Update the weather data for the panel and display 
    // the status panel, on time, delayed based on the status field
    updatePanel(nameValueParams){
        this.noDataStatusPanel.hide()

        if (nameValueParams['status'] === 0 ){
            this.timeDisplayElement.classed("flight-predict-delay", false);
            this.timeDisplayElement.classed("flight-predict-on-time", true);
            this.delayedStatusPanel.hide(); 
            this.ontimeStatusPanel.show()
            this.ontimeStatusPanel.updatePanel(nameValueParams);
        }
        else {
            this.timeDisplayElement.classed("flight-predict-on-time", false);
            this.timeDisplayElement.classed("flight-predict-delay", true);
            this.ontimeStatusPanel.hide();
            this.delayedStatusPanel.show();
            this.delayedStatusPanel.updatePanel(nameValueParams);
        }
    }

    // Display the blank status panel
    clear(){
        this.timeDisplayElement.classed("flight-predict-on-time", false);
        this.timeDisplayElement.classed("flight-predict-delay", false);
        this.ontimeStatusPanel.hide();
        this.delayedStatusPanel.hide();
        this.noDataStatusPanel.show();
    }

}

// this contains all the flight display panels
// One for each hour displayed on the dashboard
class FlightDataDisplay {

    constructor(panelCount, idTemplate){
        this.panelArray = new Array(panelCount)

        for (let index=0; index < panelCount; index++){
            this.panelArray[index] = new FlightDataDisplayPanel(idTemplate + "_" + index);
        }
    }

    // Update all the hourly display panels
    updateDisplay(flightData){
        for(let index=0; index < flightData.length; index++){
            this.panelArray[index].updatePanel(flightData[index]);
        }
    }

    // Display the blanck flight data display
    clear(){
        let panel;
        for(let index=0; index < this.panelArray.length; index++){
            panel = this.panelArray[index];
            panel.clear();
        }
    }
}