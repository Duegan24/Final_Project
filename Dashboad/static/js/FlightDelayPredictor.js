// Assign event handlers to select controls
let select_origin_states = d3.select("#origin_states");
select_origin_states.on("change", function (){
    onChangePopulateSelectCtrl("origin_airports", "/get_select_opts_origin_airports?origin_state=[0]", [d3.event.target.value]);
});

let select_origin_airports = d3.select("#origin_airports");
select_origin_airports.on("change", function(){
    onChangePopulateSelectCtrl("dest_states", "/get_select_opts_dest_states?origin_airport_code=[0]", [d3.event.target.value]);
});

let select_dest_states = d3.select("#dest_states");
select_dest_states.on("change", function(){

    let originAirportCode = getSelectedOption(select_origin_airports);
    let destState = d3.event.target.value;
    let urlParamValues = [originAirportCode, destState];
    
    onChangePopulateSelectCtrl("dest_airports", "/get_select_opts_dest_airports?origin_airport_code=[0]&dest_state=[1]", urlParamValues);
});

let select_dest_airports = d3.select("#dest_airports");
select_dest_airports.on("change", function(){

    let originAirportCode = getSelectedOption(select_origin_airports);
    let destAirportCode = d3.event.target.value;
    let urlParamValues = [originAirportCode, destAirportCode];
    
    onChangePopulateSelectCtrl("dest_airlines", "/get_select_opts_dest_airlines?origin_airport_code=[0]&dest_airport_code=[1]", urlParamValues);
});

let select_dest_airlines = d3.select("#dest_airlines");
select_dest_airlines.on("change", function(){

    deleteSelectOptions("dest_dates");
     
    if (d3.event.target.value === "" || d3.event.target.value === null){
        return;
    }

    let dataArray = [""];
    let date;

    for (index = 1; index < 32; index++) {
        date = "1/" + index + "/2021";
        dataArray[index] = [date,date];
    }

    populateSelectOptions("dest_dates", dataArray);
});


let select_dest_date = d3.select("#dest_dates");
select_dest_date.on("change", function(){

    let originAirportCode = getSelectedOption(select_origin_airports);
    let destAirportCode   = getSelectedOption(select_dest_airports);
    let travel_date = encodeURI(d3.event.target.value);
    let url = "/get_flight_predict_data?origin_airport_code=[0]&dest_airport_code=[1]&travel_date";
    let urlParamValues = [originAirportCode, destAirportCode, travel_date];
    
    getDataAsync(url, urlParamValues, (dataArray) => {
        let cellIdTemplate = "#flight_delay_col_";
        let index = 0;

        dataArray.forEach((value) => {
            
            cellId = cellIdTemplate + index;

            if (value === 0) { 
                d3.select(cellId).classed("flight-predict-ontime", true);
            }
            else {
                d3.select(cellId).classed("flight-predict-delay", true);
            }

            index++
        });
    });



    onChangePopulateSelectCtrl("dest_airlines", "/get_flight_predict_data?origin_airport_code=[0]&dest_airport_code=[1]&travel_date", urlParamValues)
});

function populateSelectOptions(selectCtrlId, dataArray){
    
    d3Select = d3.select("#" + selectCtrlId)
 
    if (dataArray !== null){

        // Append select options to the select object for each row of data
        dataArray.forEach((rowArray) => {
            optionText = rowArray[0];
            optionValue = rowArray[1]
            d3Select.append("option").attr("value", optionValue).text(optionText)});
    }
}

function getSelectedOption(d3Select){
    d3Select = d3Select._groups[0][0];
    let selectOption;
    for (index = 0;; index++){
        selectOption = d3Select[index.toString()]

        if (selectOption === undefined){
            return null;
        }
        if (selectOption.selected === true){
            return selectOption.value;
        }
    }

}

function deleteSelectOptions(selectId){

    select = document.getElementById(selectId);

    for (i = select.length - 1; i >= 0; i--) {
        select.remove(i);
    }

}

let selectCtrlIdsCascadeArray = ["origin_states", "origin_airports", "dest_states", "dest_airports", "dest_airlines", "dest_dates"];

function deleteCascadeSelectsOptions(selectPopulateId){

    clearNextSelectId = false

    selectCtrlIdsCascadeArray.forEach((selectId) => {

        if (clearNextSelectId === false){
            if (selectId === selectPopulateId){
                clearNextSelectId = true
            }
            else {
                return;
            }
        }

        deleteSelectOptions(selectId)

     });
 }

function getDataAsync(url, urlParamValues, callbackFunction){

    let paramValue;

    if (urlParamValues !== undefined && urlParamValues !== null){
        for (index = 0; index < urlParamValues.length; index++){

            paramValue = urlParamValues[index];

            //If a parameter value is blank then the blank select 
            //option has been selected and the d3 request will 
            //return an empty dataArray so just return here. 
            if (paramValue.length === 0 || paramValue === null){
                return null;
            }

            url = url.replace("[" + index + "]", encodeURI(urlParamValues[index]))
        }
    }

    d3.json(url, callbackFunction);
}

function onChangePopulateSelectCtrl(selectCtrlId, url, urlParamValues){
    deleteCascadeSelectsOptions(selectCtrlId)
    getDataAsync(url, urlParamValues,(dataArray) => {
        populateSelectOptions(selectCtrlId, dataArray);
    });
}

// On page load - populate origin_states select control
onChangePopulateSelectCtrl("origin_states", "/get_select_opts_origin_states");


