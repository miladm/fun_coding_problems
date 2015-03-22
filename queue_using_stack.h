// PROBLEM:
//   Using C++ and only using the STL stack class (#include <stack>), design a
//   queue class (a.k.a. FIFO). You can only #include the <stack> class, nothing
//   else.
//
// Author: Milad Mohammadi

#include <stack>

class queue : public stack {
    public:
        queue () {}
        ~queue () {}

        void push_back (int elem) {
            _in.push_back (elem);
        }

        int pop_front () {
            in_to_out_swap ();
            int front = _out.pop_back ();
            out_to_in_swap ();
            return front;
        }

        int front () {
            in_to_out_swap ();
            int front = _out.back ();
            out_to_in_swap ();
            return front;
        }

        int back () {
            return _in.back ();
        }

        bool empty () {
            if (_in.empty ()) 
                return true;
            return false;
        }

        int size () {
            return _in.size ();
        }

    private:
        void out_to_in_swap () {
            stack<int>::iterator it;
            for (it = _out.begin (); it != _out.end (); it++) {
                _in.push_back (*it);
            }
            while (!_out.empty ()) {
                _out.pop_back ();
            }
        }
        void in_to_out_swap () {
            stack<int>::iterator it;
            for (it = _in.begin (); it != _in.end (); it++) {
                _out.push_back (*it);
            }
            while (!_in.empty ()) {
                _in.pop_back ();
            }
        }

    privte:
        stack<int> _in;
        stack<int> _out;
};
