const state = ref(true);

function isFirstTime(){
    if(localStorage.getItem("isFirstTime")){
        return true;
    }
    else{
        localStorage.setItem("isFirstTime", state)
        return false;
    }
}

export{
    isFirstTime
}