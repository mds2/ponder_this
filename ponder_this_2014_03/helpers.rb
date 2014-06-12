class Fixnum
  def factor
    result = []
    remaining = self
    try_to_divide_by = 2
    while remaining > 1
      while (remaining % try_to_divide_by) == 0
        result << try_to_divide_by
        remaining = remaining / try_to_divide_by
      end
      try_to_divide_by += 1
    end
    return result
  end

  def gcd(b)
    if b == 0
      return self
    end
    return b.gcd(self % b)
  end

  def orbit_modulo(n)
    return 0.upto(n).map{|i| (self * i) % n}
  end

  def inverses_modulo(n)
    return 0.upto(n).find_all{ |i| ((self * i) % n) == 1}
  end

  def digits
    remaining = self
    result = []
    while remaining > 0
      result << (remaining % 10)
      remaining = remaining / 10
    end
    return result
  end
end


