#include <stdio.h>
#include <gsl/gsl_multimin.h>

// Define the Rosenbrock function
double rosenbrock(const gsl_vector *v, void *params) {
    double x = gsl_vector_get(v, 0);
    double y = gsl_vector_get(v, 1);

    return (1 - x) * (1 - x) + 100 * (y - x * x) * (y - x * x);
}

int main(void) {
    const gsl_multimin_fminimizer_type *T;
    gsl_multimin_fminimizer *s;

    // Starting point
    gsl_vector *x = gsl_vector_alloc(2);
    gsl_vector_set(x, 0, 0.0);
    gsl_vector_set(x, 1, 0.0);

    // Set the minimization function and starting point
    gsl_multimin_function minfunc;
    minfunc.n = 2;
    minfunc.f = &rosenbrock;
    minfunc.params = NULL;

    // Choose the minimization algorithm
    T = gsl_multimin_fminimizer_nmsimplex2;
    s = gsl_multimin_fminimizer_alloc(T, 2);
    gsl_multimin_fminimizer_set(s, &minfunc, x, 0.01, 1e-4);

    // Perform the minimization
    int status;
    int iter = 0;
    do {
        iter++;
        status = gsl_multimin_fminimizer_iterate(s);
        if (status)
            break;

        double size = gsl_multimin_fminimizer_size(s);
        status = gsl_multimin_test_size(size, 1e-4);

        if (status == GSL_SUCCESS) {
            printf("Converged to minimum at:\n");
        }

        printf("Iteration %d: x = %g, y = %g, f(x,y) = %g, size = %g\n",
               iter, gsl_vector_get(s->x, 0), gsl_vector_get(s->x, 1),
               s->fval, size);

    } while (status == GSL_CONTINUE && iter < 100);

    // Free allocated memory
    gsl_vector_free(x);
    gsl_multimin_fminimizer_free(s);

    return 0;    m,
}