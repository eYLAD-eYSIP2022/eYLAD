
function startTour() {
  if (document.URL.includes("dashboard")) {
    var steps = [
      {
        title: "Welcome",
        content: "<p>Welcome to the Guided Tour !!</p>"
      },{
        id: "tour-navbar",
        title: "Navbar !!",
        content: "<p>Dropdown for changing the theme and Logout button !!</p>"
      },{
        id: "sidebar",
        title: "Other Pages !!",
        content: "<p>Want more info regarding tasks, click me.</p>"
      },{
        id: "tour-prediction",
        title: "Predicting Results",
        content: "<p>Stats of how many teams have submmitted the tasks and also a <b>prediction</b> of teams expected to submit.</p>"
      },{
        id: "tour-discourse",
        title: "Discourse Stats",
        content: "<p>Major Discourse Statistics.</p>"
      },{
        id: "tour-feedback-all",
        title: "Feedback Data",
        content: "<p>Box plot of various questions of Feedback Form.</p>"
      },{
        id: "tour-feedback-ques",
        title: "Detailed Feedback",
        content: "<p>More detailed representation of Feedback data Question-wise.</p>"
      },{
        id: "tour-feedback-comments",
        title: "Feedback Comments",
        content: "<p>See the comments from the participants.</p>"
      },{
        id: "tour-informed-teams",
        title: "Informed Teams Counter",
        content: "<p>See the data of how many teams had seen a particular post/topic on Discourse</p>"
      }
    ];
  }
  else {
    var steps = [
      {
        // id: "tour-task-submitted",
        title: "Start Tour !!",
        content: "<p>Allow me to introduce you to the website.</p>"
      },{
        id: "tour-task-submitted",
        title: "Submitted Teams",
        content: "<p>Get the data of teams that have submitted the previous task vs teams that have submitted this task.</p>"
      },{
        id: "tour-task-prediction",
        title: "Prediction Results",
        content: "<p>Stats of how many teams have submmitted the tasks and also a <b>prediction</b> of teams expected to submit.</p>"
      },{
        id: "tour-task-metrics",
        title: "Prediction Metrics",
        content: "<p>Get to know about the model used for prediction.</p>"
      },{
        id: "tour-task-login",
        title: "Login Stats",
        content: "<p>Number of teams logging in for past 10 days.</p>",
      },{
        id: "tour-task-predicted-results",
        title: "Predicted Results",
        content: "This provides team-wise predictions for the given task",
      },{
        id: "tour-task-submitted-teams",
        title: "Submitted teams",
        content: "Details of the teams that have submitted the task.",
      }
    ]
  }
  var tour = new Tour(steps);

  tour.show();
}