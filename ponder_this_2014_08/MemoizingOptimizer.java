import java.lang.String;
import java.util.Arrays;

public class MemoizingOptimizer
{

    /** The ith entry of this is the numerator for the min expected
     *  cost of optimizing
     *  among i contiguous values.
     *
     *  The corresponding denominator is "i"
     */
    int numerators [];

    /** Primarily for debugging, or for attempting to find patterns
     *  in the problem.
     */
    int split_choices [];

    int cost_positive_answer;
    int cost_negative_answer;


    public MemoizingOptimizer (int cost_less, int cost_greater_equal)
    {
	cost_positive_answer = cost_greater_equal;
	cost_negative_answer = cost_less;
    }

    boolean PopulateCostsUpTo (int num_elements)
    {
	if (numerators == null) {
	    numerators = new int [2];
	    split_choices = new int [2];
	    numerators [0] = 0;
	    numerators [1] = 0; // because you already know where it is.
	    split_choices [0] = 0; // fairly meaningless.
	    split_choices [1] = 0; // fairly meaningless.
	}
	if (numerators.length > num_elements) {
	    return true;
	}
	int old_size = numerators.length;
	numerators = Arrays.copyOf (numerators, num_elements + 1);
	split_choices = Arrays.copyOf (split_choices, num_elements + 1);

	for (int size = old_size; size < numerators.length; ++size) {
	    int best_min = cost_negative_answer +
		(size - 1) * cost_positive_answer +
		numerators [size - 1];
	    int best_split = 1;
	    for (int split = 2; split < size; ++split) {
		int current_min =
		    split * cost_negative_answer +
		    numerators [split] +
		    (size - split) * cost_positive_answer +
		    numerators [size - split];
		if (current_min < best_min) {
		    best_min = current_min;
		    best_split = split;
		}
	    }
	    numerators [size] = best_min;
	    split_choices [size] = best_split;
	}
	return true;
    }

    public int NumeratorCostFor (int num_elements)
    {
	PopulateCostsUpTo (num_elements);
	return numerators [num_elements];
    }

    public int DenominatorCostFor (int num_elements)
    {
	return num_elements; // (d'uh)
    }

    public int BestSplitChoiceFor (int num_elements)
    {
	PopulateCostsUpTo (num_elements);
	return split_choices [num_elements];
    }

    public static void main (String [] argv)
    {
	int cost_greater_equal = 10;
	int cost_less = 1;
	int cost_to_compute = 100;
	if (argv.length > 0)
	    cost_greater_equal = Integer.parseInt (argv[0]);
	if (argv.length > 1)
	    cost_less = Integer.parseInt (argv[1]);
	if (argv.length > 2)
	    cost_to_compute = Integer.parseInt (argv[2]);

	MemoizingOptimizer m = new MemoizingOptimizer (cost_less,
						       cost_greater_equal);
	System.out.format ("Costs are %d, %d\n",
			   cost_less, cost_greater_equal);
	for (int i = cost_to_compute; i > 0; --i) {
	    System.out.format ("%d\t%d\t%d\t%g\t%s\n",
			       i, m.BestSplitChoiceFor (i),
			       m.NumeratorCostFor (i),
			       m.NumeratorCostFor (i) / (1.0 * i),
			       (m.NumeratorCostFor (i) % i == 0 ?
				"*" : ""));
	}
    }
}
