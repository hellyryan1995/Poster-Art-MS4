var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#5B5B5B',
        fontFamily: '"Work Sans", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '15px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#A74646',
        iconColor: '#A74646'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');