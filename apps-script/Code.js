var NOTIFY_EMAIL = "contact.matt.gibson@gmail.com";

function doPost(e) {
  var data = e.parameter;

  // honeypot: bots fill hidden fields, humans don't
  if (data.website) {
    return ContentService.createTextOutput("Success");
  }

  if (data.formType === "newsletter") {
    handleNewsletter(data);
  } else if (data.formType === "contact") {
    handleContact(data);
  }

  return ContentService.createTextOutput("Success");
}

function handleNewsletter(data) {
  var sheet = getOrCreateSheet("Newsletter");
  sheet.appendRow([new Date(), data.email]);

  MailApp.sendEmail({
    to: NOTIFY_EMAIL,
    subject: "New newsletter subscription",
    body: "New subscriber:\n\nEmail: " + data.email
  });
}

function handleContact(data) {
  var sheet = getOrCreateSheet("Contact");
  sheet.appendRow([new Date(), data.name, data.email, data.message]);

  MailApp.sendEmail({
    to: NOTIFY_EMAIL,
    subject: "New contact message from " + data.name,
    body: "Name: " + data.name + "\nEmail: " + data.email + "\n\n" + data.message
  });
}

function getOrCreateSheet(name) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  return ss.getSheetByName(name) || ss.insertSheet(name);
}
