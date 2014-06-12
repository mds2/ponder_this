load 'State.rb'

class Solution
  attr_accessor :size, :states, :expectation, :prob_sum

  def initialize(num_cells)
    @size = num_cells
    @expectation = 0
    @states = []
  end

  def explore!()
    @expectation = 0
    @prob_sum = 0
    @states = []
    first_state = State.new([], 1)
    frontier = {first_state.key => first_state}
    frontier_plus_2 = {}
    frontier_plus_4 = {}
    while not frontier.empty?
      for key, state in frontier
        if state.is_final?(@size)
          @expectation += state.expectation_contribution
          @prob_sum += state.prob
        else
          state_plus_2, state_plus_4 = state.reproduce
          if state_plus_2.sum != (2 + state.sum) or
              state_plus_4.sum != (4 + state.sum)
            puts "There is an error in computing next states"
          end
          frontier_plus_2[state_plus_2.key] =
            state_plus_2.combine(frontier_plus_2[state_plus_2.key])
          frontier_plus_4[state_plus_4.key] =
            state_plus_4.combine(frontier_plus_4[state_plus_2.key])
        end
        @states << state # unnecessary except for debugging
      end
      frontier = frontier_plus_2
      frontier_plus_2 = frontier_plus_4
      frontier_plus_4 = {}
    end
  end

  def compute_expectation!()
    self.explore!()
    return @expectation
  end
end
