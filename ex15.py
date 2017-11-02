def analyse_song(s):
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz ':
                ans = ans + c

        charsList = []
        for char in ans:
            split = ans.split(" ")

        return create_dictionary(split)

    def create_dictionary(s):
        dict = {}
        for i in range(0,len(s)):
            if s[i] not in dict:
                dict.update({s[i]:1})
            else:
                dict[s[i]] += 1

        return dict

    return to_chars(s)

s="Just somethin' about you Way I'm lookin at you whatever keep lookin at me Gettin' scared now, right? Don't fear me baby, it's just Justin It feel good right? Listen I kind of noticed something wasn't right In your colorful face It's kind of weird to me Since you're so fine If it's up to me your face'll change..... If you smilin', that should set the tone Just be limberAnd If you let go, the music should groove your bones Just remember Sing this song with me Ain't nobody love you like I love you You're a good girl and that's what makes me trust ya Late at night, I talk to you You will know the difference when I touch you People are so phony Nosy cause they're lonely Aren't you sick of the same thing? They say so and so was dating Love you or they're hating When it doesn't matter anyway Cause we're here tonight If you smiling, that should set the tone Just be limber baby And If you let go, the music should groove your bones Baby just remember Sing this song with me Ain't nobody love"

print(analyse_song(s))
