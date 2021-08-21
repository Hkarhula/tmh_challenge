# tmh_challenge

In this file I shall keep a running commentary of my approach.
Usually I don't keep this kind of file, but I believe this will provide valuable insight to my approach that is likely to go unnoticed otherwise.

## (Planned) Steps

1. create git repo, done
2. document initial thoughts, done
3. work on the challenge, started
4. code documentation
5. document closing thoughts

## Initial thoughts

The challenge seems quite straight forward, except for a few details.
I'm planning to work on this for 90 minutes today and see if I shall invest more into it.

The meter is to provide random but continuous values. For now I'm planning a wave function with some noise, I hope that satisfies the requirements well enough.
I'll need to work on a broker - not so trivial - I have no valuable experience with rabbitMQ. I think I will just create a mock broker here - all it really has to do is provide timestamps of one day.
For the PV simulator I think I will use the max of two parabolic functions and add some noise. I don't know enough about such systems to create a proper simulation, but I believe I'll te close enough to the picture provided.
Writing output to a file should be easy. I believe I'll create a dataclass for the data, such that I have a neat storage for the timestamp as well.

Not sure about testing yet. This problem seems so small at the moment that I foresee just a single test, which just runs the code and checks the output.

## Working on it

I created a powerValue dataclass, for now unused
I also created the pvSimulator - I assume a visualization of the functionality should be done to assert its behaviour, but I don't intend to invest time on that now.

I'll stop for today. I guess I will come back to this after all.
Next steps should be creating the meter and the broker.
Then we'll need a file to run everything and write the data to file.

Am I expected to write a dockerfile to make execution easier?