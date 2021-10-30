# Poster Art

Poster Art is an E-commerce business based around selling digital abstract art pieces printed at the highest quality once the order has been made.

Users can choose between a variety of different themed abstract art and what size they want to be printed, if they wish to frame it they can also purchase a frame.

My application features e-commerce functionality, payments using stripe, confirmation emails, CRUD functionality for admin to add blog posts and stock items, and an admin section, for the admin user to access database records.

* for the accessor I have included admin login details in the comment section when submitting the project.

* To test purchase products type 4242 4242 4242 4242

[>> View the live site here <<](https://rh-poster-art-ms4.herokuapp.com/)

![](static/images/home-mockup.png)

## UX

Poster Art is a minimal design website where users can select and purchase from a range of abstract art prints so the main focus is to provide users with clear buttons directly to the prints page.

The main design of the website is black and white allowing the colours from the abstract art to shine through.

### User's goal

* View and purchase posters.
* Sort through by name, price etc.
* Easily navigate through the website.
* Visually pleasing.

### Site owners goal

* Allow users to sign up to the website.
* Add, Edit and Delete products.
* Search for products.

### User's Stories

**As a user visiting the website I want:**

* To be able to easily navigate the website.
* Create an account to store my shipping details.
* Logout.
* Sign in to my existing account.
* Search for posters.
* Purchase posters and frames.
* View new arrivals.

**As the website owner I want:**

* Users to easily be able to create an account.
* To be able to add new products.
* To edit existing products.
* To delete products.

### WireFrames

* [Poster Art - Home Page](static/images/wireframes/PosterArt-Home.png)
* [Poster Art - About Us Page](static/images/wireframes/PosterArt-About-Us-Page.png)
* [Poster Art - Posters Page](static/images/wireframes/PosterArt-Poster-Page.png)
* [Poster Art - Frames Page](static/images/wireframes/PosterArt-Frames-Page.png)
* [Poster Art - New Arrivals Page](static/images/wireframes/PosterArt-New-Arrivals-Page.png)
* [Poster Art - Sign Up Page](static/images/wireframes/PosterArt-signup-Page.png)
* [Poster Art - Login Page](static/images/wireframes/PosterArt-Login-Page.png)
* [Poster Art - Profile Page](static/images/wireframes/PosterArt-Profile-Page.png)
* [Poster Art - Cart Page](static/images/wireframes/PosterArt-cart-Page.png)
* [Poster Art - Checkout Page](static/images/wireframes/PosterArt-checkout-Page.png)

### Design Choices

**Fonts**

* All headers will be using the font Work Sans at size 900
* All paragraph, buttons & menu text will be using work sans at size 400

**Colours**

* The background will be white - #fffff
* All headers and buttons will be - #111111
* Paragraph text will be - #5B5B5B
* Menu text on home page - #fffff
* Menu text on other pages - #5B5B5B
* Promo Bar - #6D7F80
* Footer and secondary background colour - #D9D9D9

## Features

### Existing Features

* Feature 1 - A home app featuring a shop now banner taking you to the product page and a collect of the posters all linking to the specific poster designs.
* Feature 2 - A Products app displaying all products available which for super users can add and delete them.
* Feature 3 - A Profile app where logged in users can save there shipping address and view previous orders.
* Feature 4 - A login/signup app where users and login or create a new account if they dont have one already, A verification email will be sent.
* Feature 5 - A Bag app where users can view there product, size, quantity and amount.
* Feature 6 - A Checkout app where using can purchase there order.
* Feature 7 - A Blog app where users can view blog posts and comment when logged in, super users can add, edit and delete posts.
* Feature 8 - A Thank You section for after the users has purchased there order, displaying there order.
* Feature 9 - A About page giving info into the company.
* Feature 10 - Search Functionality
* Feature 11 - Pop up notification when any activity happens, reassuring users of any actions made within the website.

### Features Left to Implement

* If I had more time I wanted to add price change options depending on the product size.

## Technologies Used

* [HTML](https://en.wikipedia.org/wiki/HTML)
    * For Structuring the site.

* [CSS](https://en.wikipedia.org/wiki/CSS)
    * For Styling the Site.

* [JS](https://en.wikipedia.org/wiki/JavaScript)
    * For programming functions

* [Bootstrap](https://getbootstrap.com/)
    * For Grid Layout & Components.

* [Google Font](https://fonts.google.com/)
    * For selected font.

* [JQuery](https://jquery.com/)
    * Used for certain sections within the script.js file

* [Github](https://github.com/)
    * Storing project on.

* [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiA3smABhCjARIsAKtrg6JfbE3I-05NWUBL17jlkE6uDkROXDoD5vXo7UJxVKIjsLVwujyaus0aAhAiEALw_wcB)
    * Creating wireframes on.

* [Google Chrome Developer Tool](https://developers.google.com/web/tools/chrome-devtools)
    * Checking site is responsive on multiple different devices.

* [Affinity Designer](https://affinity.serif.com/en-gb/designer/)
    * Creating Poster Art Logo

* [Flat Icon](https://www.flaticon.com/uicons)
    * Using the Icons

* [Heroku](https://dashboard.heroku.com/apps)
    * For Deployment

* [Amazon AWS](https://aws.amazon.com/?nc2=h_lg)
    * For Storing all media and static files

* [Django](https://www.djangoproject.com/)
    * Using its framework and app

* [Stripe](https://stripe.com/en-ie)
    * For payment system

## Testing

* Devices tested on:
    * Macbook Pro 13"
    * Lg 27" Monitor
    * iPhone 11
    * All devices in inspector tool.

* Browsers Tested on:
    * Google Chrome
    * Safari
    * Firefox

### User's Stories

* The navigation is clear at the top of the site with a navbar on mobile
* Login and sign up pages are available, users logged in can access there profile page with shipping details and order history
* You can logout when finished on the website.
* Search icon displayed and when clicked displays a full bar to search for a product.
* bag and checkout page is is available for users to purchase there order.
* New Arrivals displayed within the website.
* Blog can is showing the latest posts, users can comment on the post is they wish to.
* Super users can create, update and delete products.
* Super users can create, update and delete blogs.
* email verification then users log in.

### Manual Testing

1. Buttons
    * All links follow to the correct page.
    * Responds on all devices.

2. Links
    * All links follow to the correct page.
    * Burger Menu dislpayed on mobile view.
    * All products display in there correct category.

3. Search
    * Searching shows results from title and description.

    ![](static/images/testing/search-results.png)

4. Products
    * All product display in there correct category.

    ![](static/images/testing/category.png)

    * Product Ammount per page is displayed within the top left of the page.
    * Click the product takes you to the product in full detail where you can select the size and quantity.
    * Clicking add to cart send to bag and quanity amount is displayed on the bag icon.
    ![](static/images/testing/bag-icon.png)

5. Bag
    * Updating the quantity with increase the total price.
    ![](static/images/testing/quantity.png)

    * Bags under the price of €50 will be displayed with a text info on how much to spend for free shipping.
    ![](static/images/testing/free-shipping.png)

6. Checkout
    * Filling in the contact info and submiting without a correct email prompts a warning.
    ![](static/images/testing/incorrect-form.png)

    * When for is correct we are sent to a thank you page with a success message.
    ![](static/images/testing/thank-you.png)

7. Profile
    * Within profile users delivery information is saved and can be updated.
    ![](static/images/testing/save-info.png)
    * Order history is also displayed.

8. Pop Up
    * When products are added to the cart then a success message pops up.
    ![](static/images/testing/pop-up.png)

9. Login/Register
    * Users can easily Login by providing there username and password.
    * User registering to the site provides email, username and password, If re enter email or password is incorrect and error is displayed.
    ![](static/images/testing/register-login.png)

    * When registered you will recieve a verification email to confirm you account.
    ![](static/images/testing/confirm-email.png)

10. Super Users
    * When a super users is logged in they recieve access to product managment and blog management.
    ![](static/images/testing/super-user.png)

    * within product management users can add a new product by filling in the form.
    ![](static/images/testing/product-fill-up.png)

    * Clicking add, adds the products.
    ![](static/images/testing/product-add.png)

    * This works the same for posts.
    * within the product, super users can also edit and delete the product.
    ![](static/images/testing/edit-delete.png)

    * Clicking edit takes you to the form with the product info save in there.
    ![](static/images/testing/edit-product.png)

    * Clicking delete removes product.
    ![](static/images/testing/delete-product.png)

### Testing Code

* W3C Markup Validator
    * [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Frh-poster-art-ms4.herokuapp.com%2F)
    * [Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Frh-poster-art-ms4.herokuapp.com%2Fproducts%2F)
    * [Blog](https://validator.w3.org/nu/?doc=https%3A%2F%2Frh-poster-art-ms4.herokuapp.com%2Fblog%2F)
    * [Profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Frh-poster-art-ms4.herokuapp.com%2Fprofile%2F)
    * [Sign In](https://validator.w3.org/nu/?doc=https%3A%2F%2Frh-poster-art-ms4.herokuapp.com%2Faccounts%2Flogin%2F)
    * [Bag](https://validator.w3.org/nu/?doc=https%3A%2F%2Frh-poster-art-ms4.herokuapp.com%2Fbag%2F)
    * [Checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Frh-poster-art-ms4.herokuapp.com%2Fcheckout%2F)

* W3C CSS Validator

![CSS Validator Results](static/images/testing/css-validator.png)

### Bugs Discovered

* Problem 1 - I wanted to change the price depending on the size, using this code worked but the price wouldnt carry over into the checkout page

```
// Help from Stackoverflow
var basePrice = +($('#price').html()).replace(/[^0-9\.]+/g,"");

$("#id_product_size").change(function() {
  newPrice = basePrice;
  $("#id_product_size option:selected").each(function() {
    newPrice += +$(this).attr('data-price');
  });
  $("#price").html('€' + newPrice.toFixed(2));
  var itemId = $(this).data('item_id');
  handleEnableDisable(itemId);
  console.log("Base Price", basePrice);
  console.log("New Price", newPrice);
});
```

* Problem 1 - Unfortunatley I didnt have enough time to solve it.

## Deployment

## Credits

### Content

* [This](https://www.youtube.com/watch?v=m3hhLE1KR5Q&list=PL8qSL3acJhtSnIyoGc4G2JK_nyvD5wypZ&index=1&ab_channel=CodeWithStein) was used to help me add the comments to the blog page.

### Media

* [Unsplash](https://unsplash.com/)
    * This was used for product images.

* [Pexels](https://www.pexels.com/)
    * This was used for product images.

* [Freepik](https://www.freepik.com/home)
    * This was used frame mockups.

### Acknowledgements

* Help from some students in the slack chat.
* I recieved help from the tutor support.
* Alot of help from the boutique ado lessons.