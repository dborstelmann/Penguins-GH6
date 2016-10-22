hk = hk || {};

hk.ApplyView = BB.View.extend({
    el: '#apply',
    template: _.template($('#apply-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());

        this.$('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 100 // Creates a dropdown of 15 years to control year
        });
        hk.materializeShit();
    },

    events: {
        'click .home-link': 'goHome',
        'click .submit-application': 'submitApplication'
    },

    goHome: function () {
        window.location.href = '/';
    },

    submitApplication: function () {
        var _this = this;

        var firstName = this.$el.find('#first-name').val(),
            lastName = this.$el.find('#last-name').val(),
            why = this.$el.find('#why').val(),
            phone = this.$el.find('#phone-number').val(),
            email = this.$el.find('#email').val(),
            address = this.$el.find('#address').val(),
            birthday = this.$el.find('#birthday').val(),
            race = this.$el.find('#race').val(),
            gender = this.$el.find('#gender').val(),
            veteran = this.$el.find('#veteran').val(),
            enrolledBefore = this.$el.find('#enrolled-before').val(),
            family = this.$el.find('#family').val(),
            domesticViolence = this.$el.find('#domestic-violence').val(),
            pregnancy = this.$el.find('#pregnancy').val(),
            drug = this.$el.find('#drug').val();

        if (firstName &&
            lastName &&
            why &&
            phone &&
            email &&
            address &&
            birthday &&
            race &&
            gender &&
            veteran &&
            enrolledBefore &&
            family &&
            domesticViolence &&
            pregnancy &&
            drug) {

            $.ajax({
                url: '/api/apply/',
                type: 'POST',
                data: {
                    firstName: firstName,
                    lastName: lastName,
                    why: why,
                    phone: phone,
                    email: email,
                    address: address,
                    birthday: birthday,
                    race: race,
                    gender: gender,
                    veteran: veteran,
                    enrolledBefore: enrolledBefore,
                    family: family,
                    domesticViolence: domesticViolence,
                    pregnancy: pregnancy,
                    drug: drug
                },
                success: function () {
                    window.location.href = '/submit';
                },
                error: function () {
                    Materialize.toast('Application submission failed.  Please try again later.', 2000);
                }
            });
        } else {
            Materialize.toast('Please fill all fields.', 2000);
        }
    }
});
