#include <igraph.h>
#include <stdio.h>

int main(void) {
    igraph_integer_t num_vertices = 1000;
    igraph_integer_t num_edges = 1000;
    igraph_real_t diameter;
    igraph_t graph;

    igraph_rng_seed(igraph_rng_default(), 42);

    igraph_erdos_renyi_game(&graph, IGRAPH_ERDOS_RENYI_GNM,
                            num_vertices, num_edges,
                            IGRAPH_UNDIRECTED, IGRAPH_NO_LOOPS);

    igraph_diameter(&graph, &diameter, NULL, NULL, NULL, NULL, IGRAPH_UNDIRECTED, /* unconn= */ true);
    printf("Diameter of a random graph with average degree %g: %g\n",
            2.0 * igraph_ecount(&graph) / igraph_vcount(&graph),
            (double) diameter);


     // Step 1: Declare a FILE pointer
    FILE *file;

    // Step 2: Open the file in write mode ("w")
    file = fopen("igraph_test.gml", "w");

    // Step 3: Check if the file was opened successfully
    if (file == NULL) {
        printf("Failed to create the file.\n");
        return 1; // Exit the program with an error code
    }

    /* Output as GML */
    igraph_write_graph_gml(&graph, file, IGRAPH_WRITE_GML_DEFAULT_SW,  0, "");

    // Step 4: Close the file
    fclose(file);

    igraph_destroy(&graph);

    return 0;
}