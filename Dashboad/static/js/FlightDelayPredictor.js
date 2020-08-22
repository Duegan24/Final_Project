let selectCtrlIdsArray = ["origin_states", "origin_airports", "dest_states"]

// Assign event handlers to select controls
d3.select("#origin_states").on("change", onChangeOrigStatesEventHandler);

//d3.select("#origin_airports").on("change", onChangeOrigAirportsEventHandler);

// On page load - populate origin_states select control
onChangePopulateSelectCtrl("origin_states", "/get_select_opt_origin_states")





function clearSelectOptions(selectPopulateId){

    clearNextSelectId = false

    selectCtrlIdsArray.forEach((selectId) => {

        if (clearNextSelectId === false){
            if (selectId === selectPopulateId){
                clearNextSelectId = true
            }
            else {
                return;
            }
        }

        select = document.getElementById(selectId);

        for (i = select.length - 1; i >= 0; i--) {
            select.remove(i);
        }
    });
 }

 
function onChangePopulateSelectCtrl(selectCtrlId, url, urlParamValues){

    if (urlParamValues !== undefined && urlParamValues !== null){
        for (index = 0; index < urlParamValues.length; index++){
            url = url.replace("[" + index + "]", encodeURI(urlParamValues[index]))
        }
    }

    clearSelectOptions(selectCtrlId)


    d3.json(url, (dataArray) => {
 
        d3Select = d3.select("#" + selectCtrlId)
 
        if (dataArray !== null){

            // Append select options to the select object for each row of data
            dataArray.forEach((rowArray) => {d3Select.append("option").attr("value", rowArray[1]).text(rowArray[0])});
        }
    
    });
}


function onChangeOrigStatesEventHandler(){
    onChangePopulateSelectCtrl("origin_airports", "/get_select_opt_origin_airports?origin_state=[0]", [d3.event.target.value], ["dest_states"])
}

