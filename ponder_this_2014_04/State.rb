class State
  attr_accessor :prob, :state

  def initialize(statevec, prob)
    @prob = prob
    @state = statevec
  end

  def compactify_once!()
    if @state.length < 1
      return self
    end
    accum = []
    remain = @state
    number_to_try = remain.pop
    while not remain.empty?
      if number_to_try != remain.last
        accum << number_to_try
        number_to_try = remain.pop
      else
        number_to_try += remain.pop
      end
    end
    accum << number_to_try
    @state = accum.reverse
    return self
  end

  def compactify!
    old_length = @state.length
    new_length = compactify_once!.state.length
    while new_length != old_length
      old_length = new_length
      new_length = compactify_once!.state.length
    end
    return self
  end

  def reproduce()
    return [State.new([2] + @state, Rational(1,2) * prob).compactify!(),
    State.new([4] + @state, Rational(1,2) * prob).compactify!()]
  end

  def add_front(list, prob_multiplier)
    return State.new(list + @state, prob * prob_multiplier).compactify!
  end

  def combine(other_state)
    if other_state == nil
      return self
    end
    return State.new(@state, @prob + other_state.prob)
  end

  def key()
    return "a" + @state.map{|x| String(x)}.join(".")
  end

  def sum()
    return @state.reduce(0){|x,y| x + y}
  end

  def is_final?(max_length)
    return @state.length >= max_length
  end

  def expectation_contribution()
    return @state.max * @prob
  end

end


