class FlightDataStatusPanel{
idTemplate
    constructor(id, isBlank, isOnTime){

        this.panel = d3.select("#" + id + (isBlank?"_blank":isOnTime?"_on_time":"_delayed"));;

        if (isBlank){
            return;
        }

        let panelValuesIdPrefix = "#" + id + (isOnTime?"_on_time_":"_delayed_");

        this.cloudiness         = d3.select(panelValuesIdPrefix + "cloudiness");
        this.precipitation      = d3.select(panelValuesIdPrefix + "precipitation");
        this.wind               = d3.select(panelValuesIdPrefix + "wind");
        this.humidity           = d3.select(panelValuesIdPrefix + "humidity");
        this.visibility         = d3.select(panelValuesIdPrefix + "visibility");

    }

    show(){
        this.panel.classed("hide", false);
        this.panel.classed("show", true);
    }

    hide(){
        this.panel.classed("show", false);
        this.panel.classed("hide", true);
    }

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


class FlightDataDisplayPanel {

    constructor(id){

        this.timeDisplayElement = d3.select("#" + id + "_time");

        this.noDataStatusPanel = new FlightDataStatusPanel(id, true, false);
        this.ontimeStatusPanel = new FlightDataStatusPanel(id, false, true);
        this.delayedStatusPanel = new FlightDataStatusPanel(id, false, false);
        this.clear();
    }

    updatePanel(nameValueParams){
        this.noDataStatusPanel.hide()

        if (nameValueParams['status'] === 1 ){
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

    clear(){
        this.timeDisplayElement.classed("flight-predict-on-time", false);
        this.timeDisplayElement.classed("flight-predict-delay", false);
        this.ontimeStatusPanel.hide();
        this.delayedStatusPanel.hide();
        this.noDataStatusPanel.show();
    }

}


class FlightDataDisplay {

    constructor(panelCount, idTemplate){
        this.panelArray = new Array(panelCount)

        for (let index=0; index < panelCount; index++){
            this.panelArray[index] = new FlightDataDisplayPanel(idTemplate + "_" + index);
        }
    }

    updateDisplay(flightData){
        for(let index=0; index < flightData.length; index++){
            this.panelArray[index].updatePanel(flightData[index]);
        }
    }

    clear(){
        let panel;
        for(let index=0; index < this.panelArray.length; index++){
            panel = this.panelArray[index];
            panel.clear();
        }
    }
}