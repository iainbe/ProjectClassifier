/* toolkit-sweep-launcher — executes the sweep scripts inside Google Drive.
 *
 * Why this exists: launchd children have no TCC grant for ~/Library/CloudStorage,
 * so launchd can run binaries in /bin but they get EPERM opening files under
 * CloudStorage. This binary lives OUTSIDE CloudStorage (~/bin/) so launchd can
 * exec it. Grant it Full Disk Access once (System Settings -> Privacy &
 * Security -> Full Disk Access) and its children inherit the grant.
 *
 * Usage: toolkit-sweep-launcher [trigger]
 *   (no arg)  -> tools/run_sweep.sh        (scheduled sweep)
 *   trigger   -> tools/check_sweep_trigger.sh (remote-trigger poller)
 */
#include <unistd.h>
#include <string.h>
#include <stdio.h>

#define TOOLS "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/ProjectClassifier/tools/"

int main(int argc, char **argv) {
    const char *script = "run_sweep.sh";
    if (argc > 1 && strcmp(argv[1], "trigger") == 0)
        script = "check_sweep_trigger.sh";
    char path[1024];
    snprintf(path, sizeof path, "%s%s", TOOLS, script);
    execl("/bin/bash", "/bin/bash", path, (char *)NULL);
    perror("execl");
    return 127;
}
