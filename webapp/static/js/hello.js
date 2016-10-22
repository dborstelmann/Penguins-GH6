hk = hk || {};

hk.HelloView = BB.View.extend({
    el: '#hello',
    template: _.template($('#hello-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());

        this.adminLoginView = new hk.AdminLoginView();
    },

    events: {
        'click .application-link': 'goToApplication',
        'click .admin-login': 'adminLogin'
    },

    goToApplication: function () {
        window.location.href = '/apply';
    },

    adminLogin: function () {
        this.adminLoginView.show();
    }
});

hk.AdminLoginView = BB.View.extend({
    el: '.login-modal-holder',
    template: _.template($('#login-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());

        hk.materializeShit();
    },

    show: function () {
        this.$('.login-modal').openModal();
    },

    hide: function () {
        this.$('.login-modal').closeModal();
    },

    events: {
        'click .cancel-login': 'cancelLogin',
        'click .login-click': 'loginClick'
    },

    cancelLogin: function () {
        this.hide();
    },

    loginClick: function () {
        var _this = this;

        var username = this.$el.find('#username').val(),
            password = this.$el.find('#password').val();

        if (username && password) {
            $.ajax({
                url: '/auth/login/',
                type: 'POST',
                data: {
                    username: username,
                    password: password
                },
                success: function () {
                    window.location.href = '/home';
                },
                error: function () {
                    Materialize.toast('Login Failed', 2000);
                }
            });
        } else {
            Materialize.toast('Please input all fields.', 2000);
        }

    },
});
