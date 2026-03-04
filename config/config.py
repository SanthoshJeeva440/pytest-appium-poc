import os


class Configuration:

    @classmethod
    def get_config(cls):
        """
        Import Environment Config
        """

        from config.environments import QA, DEV, STAGE, PROD

        """
        Import Device Config
        """

        from config.device import Local, Cloud, Emulator

        """
        # Read runtime values
        """
        env = os.getenv("env")
        execution = os.getenv("execution")
        platform = os.getenv("platform")

        """
        # ----------------------------
        # Environment Mapping
        # ----------------------------
        """
        env_map = {"qa": QA, "dev": DEV, "stage": STAGE, "prod": PROD}

        if env not in env_map:
            raise ValueError(f"Invalid ENV: {env}")

        env_config = env_map[env]()

        """     
        # ----------------------------
        # Execution Mapping
        # ----------------------------
        """
        execution_map = {"local": Local, "cloud": Cloud, "emulator": Emulator}

        if execution not in execution_map:
            raise ValueError(f"Invalid EXECUTION: {execution}")

        execution_class = execution_map[execution]

        """
        # ----------------------------
        # Platform Mapping
        # ----------------------------
        """
        platform_map = {"android": execution_class.Android, "ios": execution_class.IOS}

        if platform not in platform_map:
            raise ValueError(f"Invalid PLATFORM: {platform}")

        device_config = platform_map[platform]()

        return env_config, device_config
