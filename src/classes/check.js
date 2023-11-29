export async function check_compatibility(classList, user){
  const url = "https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class/detailed"
  const payload = {
      username: user
    };
    
    // Encode the payload
    const params = new URLSearchParams(payload).toString();
    
    // Perform the GET request
    fetch(`${url}?${params}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
      .then(response => response.json())
      .then(data => {
        // Handle the response data
        let coursesArray = JSON.parse(data.courses);
        for(const classInstance of classList.value){
          for(const course of coursesArray){
              if(!(classInstance.daysMeet == 'TR') != (course.days_meet == 'TR')){
                  if(classInstance.startTime == course.start_time ||  classInstance.endTime == course.start_time || classInstance.startTime == course.end_time){
                      classInstance.conflictingCourse = course.Title
                      console.log(classInstance.conflictingCourse)
                      classInstance.isCompatible = false;
                      break;
                  }else{
                    classInstance.isCompatible = true;
                  }
              }else{
                  classInstance.isCompatible = true;
              }
          }
        }
      })
      .catch(error => {
        // Handle errors
        console.error('Error:', error);
      });
}