from OperationsManager import FrontendManager

def main():
    """Main entry point for the Hospital ER Management System"""
    try:
        frontend = FrontendManager()
        frontend.run()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the application.")

if __name__ == "__main__":
    main()
