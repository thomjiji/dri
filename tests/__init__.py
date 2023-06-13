import logging
import subprocess
import time


def setup_logger() -> logging.Logger:
    # Set up logger
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter(
        "[%(levelname)s] %(name)s %(asctime)s at line %(lineno)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    log.addHandler(ch)

    return log


log = setup_logger()


def skip_if_resolve_none(func):
    def wrapper(self, *args, **kwargs):
        if self.resolve is None:
            self.skipTest("resolve object is None, skipping test.")
        else:
            return func(self, *args, **kwargs)

    return wrapper


def start_davinci_resolve_app() -> bool:
    try:
        result = subprocess.run(["open", "-a", "DaVinci Resolve"], check=True)
        time.sleep(7)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False


# class TestSuiteSetup(unittest.TestCase):
#     resolve = None
#
#     @classmethod
#     def setUpClass(cls):
#         # Code to run before all test cases in the suite
#         start_davinci_resolve_app()
#         resolve = Resolve.resolve_init()
#         project_manager = resolve.GetProjectManager()
#         if project_manager.CreateProject("Dri_Tests_Project"):
#             log.info("Created Dri_test_project")
#         cls.resolve = resolve
#
#     @classmethod
#     def tearDownClass(cls):
#         # Code to run after all test cases in the suite
#         pm = cls.resolve.GetProjectManager()
#         cp = pm.GetCurrentProject()
#         if pm.CloseProject(cp):
#             log.info("CloseProject is called")
#         if pm.DeleteProject("Dri_Tests_Project"):
#             log.info("DeleteProject is called")
#         cls.resolve.Quit()