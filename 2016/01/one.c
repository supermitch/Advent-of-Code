# include <stdio.h>
# include <stdlib.h>
# include <string.h>

int main() {


    int moves = 1;


    FILE *in_file;
    in_file = fopen("input.txt", "r");

    char *line = NULL;
    size_t len = 0;
    getline(&line, &len, in_file);

    int x = 0;
    int dx;
    int y = 0;
    int dy;
    for (char *p = strtok(line, " ,"); p != NULL; p = strtok(NULL, ", ")) {
        if (p[0] == 'L') {
            puts(p);
            sscanf(p, "L%d", &dx);
            x = x - dx;
        } else if (p[0] == 'R') {
            puts(p);
            sscanf(p, "R%d", &dx);
            x = x + dx;
        }
    }
    printf("%d", x);
    free(line);

    fclose(in_file);

    printf("Part A - {}\n");
    return 0;
}
