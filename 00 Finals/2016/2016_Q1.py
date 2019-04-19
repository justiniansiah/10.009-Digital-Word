a) App.build() allows an application to be built if a widget is returned on build()
To initialize your app with a widget tree, override the build() method in the app class and return
the widget tree which is constructed. For instance to build a layout such as in the investment question, we replaced the method with instructions to create the desired layout with labels and textboxes and a button. Then the layout itself is returned at the end.

b) widget.bind() binds an event type or a property to callback. property callbacks are called with 2 arguments (the object and the property’s newvalue) and event callbacks with one argument (the object).

c) each screen requires a seperate class which contains its own widgets, be it buttons, labels and/or textboxes. in addtion, a screen manager class is required to manages the screen.
the screens are connected to each other by changing the screenmanager.current method to change the screen to the desired screen.