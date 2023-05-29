$(document).ready(function () {
  $("#contact_form")
    .bootstrapValidator({
      // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
      feedbackIcons: {
        valid: "glyphicon glyphicon-ok",
        invalid: "glyphicon glyphicon-remove",
        validating: "glyphicon glyphicon-refresh",
      },
      fields: {
        okuuchu_name: {
          validators: {
            stringLength: {
              min: 2,
            },
            notEmpty: {
              message: "Сураныч, аты-жөнүңүздү киргизиңиз",
            },
          },
        },
        getFile: {
          validators: {
            notEmpty: {
              message: "Сураныч, сүрөт жүктөңүз",
            },
          },
        },
        gender: {
          validators: {
            notEmpty: {
              message: "Сураныч, кыз же бала экениңизди жазыңыз",
            },
          },
        },
        birth_date: {
          validators: {
            notEmpty: {
              message: "Сураныч, туулган күнүңүздү киргизиңиз",
            },
          },
        },
        klassy: {
          validators: {
            notEmpty: {
              message: "Сураныч, бүтүргөн классыңызды жазыңыз",
            },
          },
        },
        adres: {
          validators: {
            notEmpty: {
              message: "Сураныч, дарегиңизди киргизиңиз",
            },
          },
        },
        okuuchu_phone: {
          validators: {
            notEmpty: {
              message: "Сураныч, телефон номериңизди киргизиңиз",
            },
          },
        },
        ataene_name: {
          validators: {
            notEmpty: {
              message: "Сураныч, ата-энеңиздин аты-жөнүн жазыңыз",
            },
          },
        },
        ataene_phone: {
          validators: {
            notEmpty: {
              message: "Сураныч, ата-энеңиздин номерин жазыңыз",
            },
          },
        },
        jk_name: {
          validators: {
            notEmpty: {
              message: "Сураныч, жооптуу кишинин аты-жөнүн жазыңыз",
            },
          },
        },
        jk_phone: {
          validators: {
            notEmpty: {
              message: "Сураныч, жооптуу кишинин тел.номерин жазыңыз",
            },
          },
        },
        whatsapp_phone: {
          validators: {
            notEmpty: {
              message: "Сураныч, вотсап номерин жазыңыз",
            },
          },
        },
        k_sabak: {
          validators: {
            notEmpty: {
              message: "Сураныч, кызыккан сабактарыңызжы жазыңыз",
            },
          },
        },
        iygilik: {
          validators: {
            notEmpty: {
              message: "Сураныч, ийгиликтериңизди жазыңыз",
            },
          },
        },
        onor: {
          validators: {
            notEmpty: {
              message: "Сураныч, өнөрүңүздү жазыңыз",
            },
          },
        },
      },
    })
    .on("success.form.bv", function (e) {
      $("#success_message").slideDown({ opacity: "show" }, "slow"); // Do something ...
      $("#contact_form").data("bootstrapValidator").resetForm();

      // Prevent form submission
      e.preventDefault();

      // Get the form instance
      var $form = $(e.target);

      // Get the BootstrapValidator instance
      var bv = $form.data("bootstrapValidator");

      // Use Ajax to submit form data
      $.post(
        $form.attr("action"),
        $form.serialize(),
        function (result) {
          console.log(result);
        },
        "json"
      );
    });
});
