function btn_clicked(con) {
    // Make AJAX request to get random word
    fetch('/get_random_word?action='+con)
        .then(response => response.json())
        .then(data => {
            // Update the course title
            if (data.state == 0) {
                console.log("FAIIIIILL");
                document.getElementById('done').style.display = "block"
              } else {
                console.log(data)
                document.getElementById('score').textContent = `Score: ${data.score}`;
                document.getElementsByClassName('course_title')[0].innerText = data.Ref_Course_Title;
                document.getElementsByClassName('course_title')[1].innerText = data.Ass_Course_Title;
                document.getElementsByClassName('course_id')[0].innerText = data.Ref_Course_ID;
                document.getElementsByClassName('course_id')[1].innerText = data.Ass_Course_ID;
                document.getElementsByClassName('course_description')[0].innerText = data.Ref_Course_Descripition;
                document.getElementsByClassName('course_description')[1].innerText = data.Ass_Course_Descripition;
                document.getElementById('fail_percentage').textContent = `${data.Ref_Fail_Percentage} %`;
              }

        })
        .catch(error => console.error('Error fetching random word:', error));
    
}
function restart(){
    document.getElementById('overlay').style.display = "none"
    document.getElementById('score').textContent = `Score: 0`;
    fetch('/')
}
