from ui import login, register, dashboard

def start_app():
    def show_login():
        login.open_login(switch_to_register=show_register, switch_to_dashboard=show_dashboard)

    def show_register():
        register.open_register(switch_to_login=show_login)

    def show_dashboard(username, role):
        dashboard.open_dashboard(username, role)

    show_login()

if __name__ == "__main__":
    start_app()
