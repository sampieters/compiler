.data
string1_1: .asciiz "Something went wrong\00"
string2_1: .asciiz "Hello world!\n\00"
string3_1: .asciiz "Hello world!\n\00"
string4_1: .asciiz "Something went wrong\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -28
        sw      $fp, 24($sp)
        sw      $ra, 20($sp)
        sw      $4, 16($sp)
        move    $fp, $sp
        li      $8, 5
        sw      $8, 0($fp)
        # BEGIN IF CONDITION
        lw      $8, 0($fp)
        slti    $8, $8, 5
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        beq     $8,$0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string1_1
        li      $2, 4
        syscall 
        # END IF BODY
        b       $L1
        nop     
$L0:    
        # BEGIN ELSE BODY
        la      $4, string2_1
        li      $2, 4
        syscall 
        # END ELSE BODY
$L1:    
        # BEGIN IF CONDITION
        lw      $8, 0($fp)
        seq     $8, $8, 5
        sw      $8, 8($fp)
        lw      $8, 8($fp)
        beq     $8,$0, $L4
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        # BEGIN IF CONDITION
        lw      $8, 0($fp)
        seq     $8, $8, 5
        sw      $8, 12($fp)
        lw      $8, 12($fp)
        beq     $8,$0, $L2
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string3_1
        li      $2, 4
        syscall 
        # END IF BODY
        b       $L3
        nop     
$L2:    
        # BEGIN ELSE BODY
        la      $4, string4_1
        li      $2, 4
        syscall 
        # END ELSE BODY
$L3:    
        # END IF BODY
$L4:    
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 16($sp)
        lw      $ra, 20($sp)
        lw      $fp, 24($sp)
        addiu   $sp, $sp, 28
        li      $2, 10
        syscall 