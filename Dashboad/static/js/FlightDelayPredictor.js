
// Assign event handlers to select controls
origin_states = d3.select("#origin_states").on("change", onChangeOrgStatesEventHandler);

//d3.select("#origin_airports").on("change", onChangeOrgStatesEventHandler);

// On page load - populate origin_states select control
onChangePopulateSelectCtrl(origin_states, "/get_origin_states")

function clearSelectOptions(selectIdArray){

    var select
    if (selectIdArray !== null){

        selectIdArray.forEach((selectId) => {

            select = document.getElementById(selectId);

            if (select !== null){

                for (i = select.length - 1; i >= 0; i--) {
                    select.remove(i);
                }
            }
        });
    }
 }

 
function onChangePopulateSelectCtrl(selectCtrlId, url, urlParamValues, clearSelectCtrlIdArray){

    if (urlParamValues !== null){
        for (index = 0; index < urlParamValues.length; index++){
            url = url.replace("[" + index + "]", encodeURI(urlParamValues[index]))
        }
    }

    clearSelectOptions(clearSelectCtrlIdArray)


    d3.json(url, (values) => {
 
        d3Select = d3.select("#" + selectCtrlId)
 
        if (values !== null){

            // Append select options to the select object for each filter data field unique value
            originStateAirports.forEach((valueArray) => {d3Select.append("option").attr("value", valueArray[1]).text(valueArray[0])});
        }
    
    });
}


function onChangeOrgStatesEventHandler(){
    onChangePopulateSelectCtrl("dest_states", "/get_dest_states?origin_airport_code=[0]", [d3.event.target.value], ["dest_states"])
}

