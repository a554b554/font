var surveyJSON = { title: "Tell us, which one is more similar to characters in the center?", pages: [
  { name:"page1",
   questions: [
      { type: "html", "html":"<img src='./Mturk/1.png' width='200px'/><p> <img src='./Mturk/6.png' width='200px'/> <p><img src='./Mturk/100.png' width='200px'/>"},
      { type: "radiogroup","name":"fff", "choices": [ "Left", "Right" ]},
   ]},
  { name: "page2", questions: [
    { type: "radiogroup", "choices": ["Yes","No"],"isRequired": false, "name": "mvllvmUsing", title: "Do you use any MVVM framework?" },
    { type: "checkbox", choices: [ "AngularJS", "KnockoutJS", "React" ], hasOther: true, isRequired: true, name: "mvvm", title: "What MVVM framework do you use?", visible: false } ] },
  { name: "page3",questions: [
    { type: "comment", name: "about", title: "Please tell us about your main requirements for Survey library" } ] }
 ]
 // triggers: [
 //  { type: "visible", operator: "equal", value: "Yes", name: "frameworkUsing", questions: ["framework"]},
 //  { type: "visible", operator: "equal", value: "Yes", name: "mvvmUsing", questions: ["mvvm"]}
 // ]
}
