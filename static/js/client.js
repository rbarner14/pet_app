"use strict";
// Can also use:
// $(function() {

// Step 1
// This code is executed when someone clicks the "Add Item" button 
// at the top right of the shopping-item
// -------------------
    $(".add-item").on('click', function(event) {
          event.preventDefault();

          var listItem = $(".item-input").val();
          var itemHtml = "<li><span class='item-check'> </span><span class='item-text'>" + listItem + "</span><span class='item-remove'></span></li>";
      // Add the itemHtml section we created for you above to the shopping-list
          $(".shopping-list").append(itemHtml)
      // Remove the text the user entered from item-input
          $(".item-input").val("");
      
    });
// -------------------


// Step 2
// -------------------
// This code is executed when someone clicks the "X" button
// at the top right of the shopping-item
  // select shopping list, on click, apply this class on it, and apply this function
    $(".shopping-list").on('click', '.item-remove', function(event) {
      // Use event.currentTarget to remove the shopping item from the shopping list
      $(event.currentTarget).parent().remove()
    });
// -------------------
  
// Step 3
// This code is executed when someone clicks the checkbox in the shopping-item section
// -------------------
    $(".shopping-list").on('click', '.item-check', function(event) {
      // currentTarget, in this instance, is whatever is clicked.
      // Use event.currentTarget to add and remove the "complete" class to the checkbox
      $(event.currentTarget).toggleClass("complete")
    });
// -------------------

//Additional Challenges
//If you add an item with no text, it adds a blank box. This is a bug! Fix it.
//Add a counter that tells the user how many items are in your shopping list
  
// });