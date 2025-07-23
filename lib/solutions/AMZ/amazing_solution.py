import os
import threading

import solutions.AMZ.amazing as amazing


class AmazingSolution:
    def amazing_maze(self, rows, columns, maze_generation_options):
        stdin_r_fd, stdin_w_fd = os.pipe()
        stdout_r_fd, stdout_w_fd = os.pipe()
        with \
            os.fdopen(stdin_r_fd, "r") as stdin_r, \
            os.fdopen(stdout_r_fd, "r") as stdout_r, \
            os.fdopen(stdin_w_fd, "w") as stdin_w, \
            os.fdopen(stdout_w_fd, "w") as stdout_w:

            app = amazing.Main(options = maze_generation_options, stdin = stdin_r, stdout = stdout_w)
            thread = threading.Thread(target = app.run)
            thread.start()
            thread.join(timeout=0.1)  # fail fast if it crashes
            if not thread.is_alive():
                raise Exception("App crashed.")

            for line in stdout_r:
                line = line.rstrip()
                if not line or line.startswith(" "):
                    continue
                match line:
                    case "WHAT ARE YOUR WIDTH AND LENGTH":
                        stdin_w.write(f"{columns}\n")
                        stdin_w.write(f"{rows}\n")
                        stdin_w.close()
                        break
                    case prompt:
                        raise Exception(f"Unknown prompt: {prompt}")

            thread.join()
            stdout_w.close()

            maze = [line for line in stdout_r if line.rstrip()]
            return "".join(maze)








